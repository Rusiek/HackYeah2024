from flask import Blueprint, request, jsonify
import requests
import json
import os

bp_paths = Blueprint('paths', __name__)

@bp_paths.route('/', methods=['GET'])
def get_path():
  #open csv file and map it to json
  paths_array = [[
    [19.907462, 50.067538],
    [19.907236, 50.066823],
    [19.913411, 50.065849],
    [19.919037, 50.064511],
    [19.923522, 50.063847,]
  ], [
    [19.906894, 50.068029],
    [19.907437, 50.069503],
    [19.910575, 50.069032],
    [19.911385, 50.068852],
    [19.912821, 50.068238],
    [19.912638, 50.068086]
  ]]

  response_dict = {}
  response_dict['paths'] = paths_array


  return jsonify(response_dict)