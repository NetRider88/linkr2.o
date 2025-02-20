#!/usr/bin/env bash
# exit on error
set -o errexit

# Install all dependencies first
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles media geoip

# Add the current directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Navigate to the Django project directory
cd linkrAppDH

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate 