#! /bin/sh

# Optional: install the virtualenv package for python3
sudo apt-get install python3-venv

# Create the virtual environment
python3 -m venv env

# Start the virtualenv
source env/bin/activate

# Install the application-specifice packages
pip install Flask
pip install flask_restful
pip install flask_session
pip install flask_cors
