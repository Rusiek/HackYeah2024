# modules
from flask import Flask
from .Config import Config
from flask_cors import CORS


# blueprints
from app.routes.index import bp_index
from app.routes.accidents.accidents import bp_accidents
from app.routes.paths.paths import bp_paths
from app.routes.cars.cars import bp_cars
from app.routes.gpx.gpx import bp_gpx

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)
  CORS(app, supports_credentials=True)
  
  app.register_blueprint(bp_index, url_prefix='/')
  app.register_blueprint(bp_accidents, url_prefix='/accidents')
  app.register_blueprint(bp_paths, url_prefix='/paths')
  app.register_blueprint(bp_cars, url_prefix='/cars')
  app.register_blueprint(bp_gpx, url_prefix='/gpx')
  
  return app