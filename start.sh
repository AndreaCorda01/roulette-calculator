#!/bin/bash
VENV=".roulettecalculator"

if [ ! -d $VENV ]; then
    python3 -m venv $VENV
fi

# Activate the virtual environment
source $VENV/bin/activate

# Install dependencies (if any)
pip install -r requirements.txt

# Run the main.py script
python main.py