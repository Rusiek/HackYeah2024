import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  DEBUG = True
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-secret'
  