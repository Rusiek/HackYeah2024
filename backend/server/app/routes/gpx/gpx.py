from flask import Blueprint, jsonify, current_app, request, send_file, after_this_request
import pandas as pd
import gpxpy
import os

bp_gpx = Blueprint('gpx', __name__)


@bp_gpx.route('/', methods=['POST'])
def generate_gpx():
  data = request.json
  vertices = data.get('vertices', [])
  should_get_waypoints = data.get('should_get_waypoints', False)


  gpx = gpxpy.gpx.GPX()

  if should_get_waypoints:
    path_to_dangerous_points = os.path.join(os.path.dirname(__file__), '../accidents/data/accidents.csv')
    list_of_places = pd.read_csv(path_to_dangerous_points)
    list_of_places = list_of_places[['long', 'lat', 'weight']]

    for lon, lat, weight in list_of_places:
      if weight == 'S': # deadly accident
        gpx_waypoint = gpxpy.gpx.GPXWaypoint(
          latitude=lat,
          longitude=lon,
          name="Some name",
          description="Some description"
        )
        gpx.waypoints.append(gpx_waypoint)

  gpx_route = gpxpy.gpx.GPXRoute()
  gpx.routes.append(gpx_route)

  for lat, lon in vertices:
      route_point = gpxpy.gpx.GPXRoutePoint(lat, lon)
      gpx_route.points.append(route_point)

  # Write the GPX content to a file
  new_file_path =  os.path.join(os.path.dirname(__file__), 'data/route.gpx')
  with open(new_file_path, 'w') as f:
      f.write(gpx.to_xml())
      
  response = send_file(new_file_path, as_attachment=True)

  # Clean up the file after sending
  @after_this_request
  def cleanup(response):
    os.remove(new_file_path)
    return response

  return response