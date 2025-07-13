#!/bin/bash

# Check required game library installation
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed or not in PATH."
    exit 1
fi

# Attempt to import pygame and capture the exit status
if python3 -c "import pygame" &> /dev/null; then
    echo "Pygame is installed and accessible."
else
    echo "Pygame is NOT installed or not accessible for python3."
    echo "You might need to install it: sudo apt-get install python3-pygame"
fi

# Path to Python program
PYTHON_PROGRAM="./main.py"

# Run program
python3 "$PYTHON_PROGRAM"
