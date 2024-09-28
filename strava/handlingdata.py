import json
import polyline

def change_polyline_to_long_lat():
    with open('segments_info.json', 'r') as file:
        data = json.load(file)

    for key, item in data.items():
        if 'map' in item and 'polyline' in item['map']:
            polyline_data = item['map']['polyline']
            long_lat_list = polyline.decode(polyline_data)
            item['map']['polyline'] = long_lat_list

    with open('segments_info2.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    change_polyline_to_long_lat()
