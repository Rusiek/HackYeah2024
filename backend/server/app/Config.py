import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  DEBUG = True
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-secret'
  REDIS_URL = 'redis://localhost:6379/0'
  HERE_API_FLOW_URL = 'https://data.traffic.hereapi.com/v7/flow'
  HERE_API_KEY = os.environ.get('HERE_API_KEY') or ''