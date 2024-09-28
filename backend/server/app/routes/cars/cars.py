from flask import Blueprint, jsonify, current_app
import requests
import json
import os
from .util import calculate_polies

bp_cars = Blueprint('acrs', __name__)

# Area of Małopolska Voivodeship in HERE-API-friendly format
top_right_lat= 50.60218
top_right_long= 21.38695
bottom_left_lat= 48.75818
bottom_left_long= 18.99499

rects = calculate_polies(bottom_left_lat, bottom_left_long, top_right_lat, top_right_long)
file_path = os.path.join(os.path.dirname(__file__), 'data/traffic_data.json')

# Get traffic flow data for the entirety of Małopolska voivodeship
@bp_cars.route('/', methods=['GET'])
def get_cars_flow():
    if(not current_app.config.get("HERE_API_KEY")):
      return jsonify({'error': 'Authentication error', 'messege': 'No API key provided', 'code': '404'}), 404
    base_url = current_app.config.get('HERE_API_FLOW_URL')
    
    # for each rectangular area get traffic data
    result_dict = {
    'results': [],
    'sourceUpdated': ''
  }
    try:
      for poly in rects:
        params = {
        'in': f'bbox:{poly[0][1]},{poly[0][0]},{poly[1][1]},{poly[1][0]}',
        'locationReferencing': 'shape',
        'apiKey': f"{current_app.config.get('HERE_API_KEY')}"
        }
        
        res = requests.get(base_url, params=params)
        res.raise_for_status()  
        res.encoding = 'utf-8'
        data = res.json()
        result_dict['results'] += data.get('results')
        result_dict['sourceUpdated'] = data.get('sourceUpdated')
        
    except requests.exceptions.HTTPError as http_err:
      return jsonify({'error': 'HTTP error', 'messege': str(http_err), 'code': '404'}), 404
    except Exception as err:
      return jsonify({'error': 'Unexpected Error', 'messege': str(err), 'code': '404'}), 404
    
    # Write the data to a file (and if file already exists, overwrite it)
    with open(file_path, 'w') as f:
      json.dump(result_dict, f)

    return jsonify("Data fetched and saved to file"), 200