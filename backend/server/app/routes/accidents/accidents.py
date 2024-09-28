from flask import Blueprint, request, jsonify
import requests
import json
import csv
import os

bp_accidents = Blueprint('accidents', __name__)

@bp_accidents.route('/', methods=['GET'])
def get_accidents():
  #open csv file and map it to json
  path_to_csv = os.path.join(os.path.dirname(__file__), 'accidents.csv')
  with open(path_to_csv, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

  return jsonify(rows)