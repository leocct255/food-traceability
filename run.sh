#!/bin/bash

# Stop the script if command fails
set -e

# move to the project directory
cd "$(dirname "$0")"

# check if the Python virtual environment exists
if [ ! -f "venv/bin/activate" ]; then
    echo "Error: Python virtual environment not found."
    exit 1
fi

# activate the virtual environment
source venv/bin/activate

# start the Python application
python app.py
