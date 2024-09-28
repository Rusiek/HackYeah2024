import csv
import os
import json

path_to_csv = os.path.join(os.path.dirname(__file__), 'accidents.csv')
path_to_json = os.path.join(os.path.dirname(__file__), 'accidents.json')
data = []
with open(path_to_csv, 'r', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  data = list(reader)

with open(path_to_json, mode='w', encoding='utf-8') as json_file:
  
  json.dump(data, json_file, indent=4, ensure_ascii=False)
