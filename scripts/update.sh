#!/bin/bash

# update.sh
# Script to pull the latest version of UDE from GitHub

# Check if the script is being run in the UDE directory
if [ ! -d ".git" ]; then
    echo "Error: This script must be run from the UDE project directory."
    exit 1
fi

echo "Pulling the latest changes from GitHub..."

# Step 1: Fetch the latest updates from the remote repository
git fetch origin

# Step 2: Pull the latest changes into the current branch
git pull origin main

# Step 3: Install or update Python dependencies
echo "Updating Python dependencies..."
pip3 install --upgrade -r requirements.txt

# Step 4: Notify user of successful update
echo "UDE has been successfully updated to the latest version."

# Optional: Provide information on restarting UDE after the update
echo "To restart UDE, run: python3 src/main.py"
