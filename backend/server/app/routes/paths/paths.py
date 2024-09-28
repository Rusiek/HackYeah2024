from flask import Blueprint, request, jsonify
import requests
import json
import os

bp_paths = Blueprint('paths', __name__)

@bp_paths.route('/', methods=['GET'])
def get_path():
  #open csv file and map it to json
  path_array = [
    [50.067538, 19.907462],
    [50.066823, 19.907236],
    [50.065849, 19.913411],
    [50.064511, 19.919037],
    [50.063847, 19.923522]
  ]

  response_dict = {}
  response_dict['path'] = path_array


  return jsonify(response_dict)