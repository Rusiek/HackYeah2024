# modules
from flask import Flask
from .Config import Config

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)
  
  # test route - delete later
  @app.route('/')
  def index():
    return 'Hello world!'

  return app