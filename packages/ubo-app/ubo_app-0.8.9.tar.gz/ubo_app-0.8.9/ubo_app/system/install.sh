#!/usr/bin/env bash


UPDATE=false

# Parse arguments
for arg in "$@"
do
    case $arg in
        --update)
        UPDATE=true
        shift # Remove --update from processing
        ;;
        *)
        # Unknown option
        ;;
    esac
done

# Check for root privileges
if [ "$(id -u)" != "0" ]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

# Define the username
if [ -z "${USERNAME}" ]; then
  USERNAME="ubo"
fi

# Create the user
adduser --disabled-password --gecos "" $USERNAME
usermod -a -G audio,video,netdev,gpio,i2c,spi,kmem,render $USERNAME

echo "User $USERNAME created successfully."

# Install required packages
apt-get -y update
apt-get -y install \
  libcap-dev \
  libegl1 \
  libgl1 \
  libmtdev1 \
  libzbar0 \
  python3-dev \
  python3-libcamera \
  python3-alsaaudio \
  python3-picamera2 \
  python3-pip \
  python3-pyaudio \
  python3-virtualenv \
  --no-install-recommends

# Enable I2C and SPI
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

# Define the installation path
if [ -z "${INSTALLATION_PATH}" ]; then
  INSTALLATION_PATH="/opt/ubo"
fi

# Create the installation path
rm -rf "$INSTALLATION_PATH/env"
virtualenv --system-site-packages "$INSTALLATION_PATH/env"

# Install the latest version of ubo-app
if [ "$UPDATE" = true ]; then
  "$INSTALLATION_PATH/env/bin/python" -m pip install --no-index --upgrade --find-links "$INSTALLATION_PATH/_update/" ubo-app[default]
else
  "$INSTALLATION_PATH/env/bin/python" -m pip install ubo-app[default]
fi

# Set the ownership of the installation path
chown -R $USERNAME:$USERNAME "$INSTALLATION_PATH"
chmod -R 700 "$INSTALLATION_PATH"

# Bootstrap the application
"$INSTALLATION_PATH/env/bin/ubo" bootstrap

if [ "$UPDATE" = true ]; then
  # Remove the update directory
  rm -rf "$INSTALLATION_PATH/_update"
fi

# The audio driver needs a reboot to work
reboot
