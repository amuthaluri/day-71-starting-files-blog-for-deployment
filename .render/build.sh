#!/usr/bin/env bash

# Force Python 3.11 on Render
echo "python-3.11.9" > runtime.txt

# Install dependencies
pip install -r requirements.txt
