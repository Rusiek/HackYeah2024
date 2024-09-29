from flask import Flask, request, send_file
import pandas as pd
import gpxpy

app = Flask(__name__)

@app.route('/generate-gpx', methods=['POST'])
def generate_gpx():
    data = request.json
    route_points = data.get('route_points', [])
    get_waypoints = data.get('get_waypoints', [])


    gpx = gpxpy.gpx.GPX()

    if get_waypoints:
        path_to_dangerous_points = "server/app/routes/accidents/data/accidents.csv"
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

    for lat, lon in route_points:
        route_point = gpxpy.gpx.GPXRoutePoint(lat, lon)
        gpx_route.points.append(route_point)

    # Write the GPX content to a file
    with open('route_with_waypoint.gpx', 'w') as f:
        f.write(gpx.to_xml())

    print("GPX file with route and waypoint created successfully!")

# Call the function to generate the GPX file
generate_gpx()
