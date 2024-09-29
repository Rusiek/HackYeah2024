from flask import Blueprint, jsonify, current_app, request, send_file, after_this_request
import pandas as pd
import gpxpy
import os

bp_gpx = Blueprint('gpx', __name__)


@bp_gpx.route('/', methods=['POST'])
def generate_gpx():
    data = request.json
    edges = data.get('edges', [])

    if not edges:
      return jsonify({'error': {'type': 'No resource found', 'messege': 'No graph edgeList provided'}, 'code': '401 '}), 401

    vertices = []
    for edge in edges:
      if('path' not in edge): continue
      print('edge: ', edge)
      vertices.append((edge['path'][0]))
    'path' in edges[-1] and vertices.append(edges[-1]['path'][1])

    gpx = gpxpy.gpx.GPX()
    gpx_route = gpxpy.gpx.GPXRoute()
    gpx.routes.append(gpx_route)
    
    for lon, lat in vertices:
        route_point = gpxpy.gpx.GPXRoutePoint(lat, lon)
        gpx_route.points.append(route_point)

    # Write the GPX content to a file
    new_file_path = os.path.join(os.path.dirname(__file__), 'data/route.gpx')
    with open(new_file_path, 'w') as f:
      f.write(gpx.to_xml())

    response = send_file(new_file_path, as_attachment=True)

    # Clean up the file after sending
    @after_this_request
    def cleanup(response):
        return response

    return response
