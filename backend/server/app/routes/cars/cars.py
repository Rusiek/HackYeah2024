from flask import Blueprint, request, jsonify, current_app
import requests
from .util import calculate_polies

bp_cars = Blueprint('acrs', __name__)

# Area of Małopolska Voivodeship in HERE-API-friendly format
top_right_lat= 50.43324
top_right_long= 21.2812
bottom_left_lat= 49.4079
bottom_left_long= 19.48032

rects = calculate_polies(bottom_left_lat, bottom_left_long, top_right_lat, top_right_long)

# Get traffic flow data for the entirety of Małopolska voivodeship
@bp_cars.route('/', methods=['GET'])
def get_cars():
  
  if(not current_app.config.get("HERE_API_KEY")):
    return jsonify({'error': 'Authentication error', 'messege': 'No API key provided', 'code': '404'}), 404
  base_url = current_app.config.get('HERE_API_FLOW_URL')
  
  # for each rectangular area get traffic data
  result_dict = {}
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
      result_dict = {**result_dict, **data}
  except requests.exceptions.HTTPError as http_err:
    return jsonify({'error': 'HTTP error', 'messege': str(http_err), 'code': '404'}), 404
  except Exception as err:
    return jsonify({'error': 'Unexpected Error', 'messege': str(err), 'code': '404'}), 404
  return jsonify(result_dict)