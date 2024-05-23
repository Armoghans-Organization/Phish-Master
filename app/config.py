##########################################################
#  Config For All The Blueprints Models and App
##########################################################

from flask_sqlalchemy import SQLAlchemy
import secrets
import os

# Get the current working directory
cwd = os.getcwd()


class Config:
    # Generate a random secret key using secrets module
    secret_key = secrets.token_hex(16)  # Generate a 16-byte (32-character) hexadecimal token

    # Set the secret key and database URI in the app configuration
    SECRET_KEY = secret_key  # Set a random secret key for session management and CSRF protection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(cwd, 'PhishMaster.sqlite3')  # SQLite database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to reduce overhead

# Initialize SQLAlchemy without the Flask app
db = SQLAlchemy()

