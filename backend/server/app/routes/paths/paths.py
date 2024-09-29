from flask import Blueprint, request, jsonify
import requests
import json
import os
import ast

bp_paths = Blueprint('paths', __name__)
file_path = os.path.join(os.path.dirname(__file__), 'data/velo.txt')

@bp_paths.route('/', methods=['GET'])
def get_path():
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().strip()

  data = ast.literal_eval(content)

  all_paths = [[list(x) for x in array] for array in data]

  response_dict = {}
  response_dict['paths'] = all_paths

  # Use ast.literal_eval for safe evaluation
  return jsonify(response_dict)

@bp_paths.route('/<id>', methods=['GET'])
def get_path_by_id(id):
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().strip()

  # Use ast.literal_eval for safe evaluation
  data = ast.literal_eval(content)
  
  array = data[int(id)]

  array = [list(x) for x in array]

  response_dict = {}
  response_dict['path'] = array

  return jsonify(response_dict)