import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False