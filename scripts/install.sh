#!/bin/bash

# install.sh
# Installation script for Unified Desktop Environment (UDE)

# Check if the script is being run with superuser privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or with sudo."
    exit 1
fi

echo "Starting installation of UDE..."

# Step 1: Install system dependencies (for Ubuntu/Debian-based systems)
echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git xorg pulseaudio

# Step 2: Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Step 3: Set up UDE configuration directory
echo "Setting up configuration directory..."
mkdir -p ~/.config/ude
cp config/ude-config.conf ~/.config/ude/
cp config/time-based-config.conf ~/.config/ude/

# Step 4: Set up the UDE environment
echo "Setting up UDE environment..."
chmod +x src/main.py

# Step 5: Installation complete
echo "UDE installation complete. You can now configure and run the environment."
echo "To start UDE, run: python3 src/main.py"

# Optional: Provide information on how to configure UDE
echo "Configuration files are located in ~/.config/ude. Edit the 'ude-config.conf' file to customize your UDE settings."
