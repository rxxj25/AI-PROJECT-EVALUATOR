#!/bin/bash

echo "========================================"
echo "AI-Powered Project Evaluator"
echo "NatWest Hackathon 2025"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 is not installed"
    echo "Please install pip3 and try again"
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
    echo
fi

# Start the application
echo "Starting AI Project Evaluator..."
echo
echo "Dashboard will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the application"
echo

python3 run.py
