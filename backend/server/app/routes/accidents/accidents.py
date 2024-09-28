from flask import Blueprint, request, jsonify
import os
import json

bp_accidents = Blueprint('accidents', __name__)
path_to_data = os.path.join(os.path.dirname(__file__), 'data/accidents.json')

# Get accidents data for the entirety of Małopolska voivodeship
@bp_accidents.route('/', methods=['GET'])
def get_accidents():
  # get data from json file and return it
  data = None
  with open(path_to_data, mode='r', encoding='utf-8') as json_file:
    try:
      data = json.load(json_file)
    except:
      return jsonify({'error': 'The resource you requested does not exist', 'messege': 'Could not find accidents file', 'code': '404'}), 404
  return jsonify(data)