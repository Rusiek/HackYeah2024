from flask import Blueprint, request, jsonify
import os
import json

bp_accidents = Blueprint('accidents', __name__)
path_to_json = os.path.join(os.path.dirname(__file__), 'data/accidents.json')

@bp_accidents.route('/', methods=['GET'])
def get_accidents():
  # get data from json file and return it
  data = None
  with open(path_to_json, mode='r', encoding='utf-8') as json_file:
    try:
      data = json.load(json_file)
    except:
      return jsonify({'error': 'The resource you requested does not exist', 'messege': 'Could not find accidents file', 'code': '404'}), 404
  return jsonify(data)