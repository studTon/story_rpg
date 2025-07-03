#!/bin/bash

# Install required library
PACKAGE_NAME="mpg123" # Replace with the actual package name (e.g., libssl-dev, libcurl4-openssl-dev)

if dpkg -l | grep -q "$PACKAGE_NAME"; then
    echo "Package '$PACKAGE_NAME' is installed."
else
    echo "Package '$PACKAGE_NAME' is NOT installed."
    sudo apt-get install mpg123
fi

# Path to Python program
PYTHON_PROGRAM="./main.py"

# Run program
python3 "$PYTHON_PROGRAM"
