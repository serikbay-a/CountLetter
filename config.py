import os

class Config(object):
    """Config file"""
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'some-very-strong-secret-key'


