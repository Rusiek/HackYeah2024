import numpy as np
import networkit as nk
import networkx as nx
from sklearn.neighbors import KDTree
import json

with open('traffic_data.json') as f:
    data_here = json.load(f)

verticies = []
results = data_here.get('results')
idx = 1
for e in results:
    loc = e.get('location')
    shape = loc.get('shape')
    links = shape.get('links')
    for p in links:
        points = p.get('points')
        for x in points:
            verticies.append([x['lng'], x['lat']])

verticies = sorted(verticies)
eps = 1e-5
unique_verticies = [verticies[0]]

def calculate_distance(lat1, long1, lat2, long2):
    return np.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)

for i in range(1, len(verticies)):
    if calculate_distance(verticies[i][1], verticies[i][0], verticies[i-1][1], verticies[i-1][0]) > eps:
        unique_verticies.append(verticies[i])

# print(len(unique_verticies))
KDTree = KDTree(unique_verticies)

with open('strava/segments_info2.json') as f2:
    data_strava = json.load(f2)

eps = 4e-5
for key, item in data_strava.items():
    if 'map' in item and 'polyline' in item['map']:
        points = item['map']['polyline']
        for p in points:
            p = p[::-1]
            dist, ind = KDTree.query([p], k=1)
            if dist > eps:
                unique_verticies.append(p)

verticies = [unique_verticies[0]]
for i in range(1, len(unique_verticies)):
    if calculate_distance(unique_verticies[i][1], unique_verticies[i][0], unique_verticies[i-1][1], unique_verticies[i-1][0]) > eps:
        verticies.append(unique_verticies[i])

G = nx.Graph()
verticies = [(x[0], x[1]) for x in verticies]
G.add_nodes_from(verticies)

for e in results:
    loc = e.get('location')
    current_flow = e.get('currentFlow')
    shape = loc.get('shape')
    links = shape.get('links')
    for p in links:
        points = p.get('points')
        for i in range(1, len(points)):
            src = (points[i-1]['lng'], points[i-1]['lat'])
            dst = (points[i]['lng'], points[i]['lat'])
            d = calculate_distance(src[0], src[1], dst[0], dst[1])
            G.add_edge(src, dst, weight=d)
            if 'jamFactor' in current_flow:
                G[src][dst]['JF'] = current_flow['jamFactor']
            if 'speedUncapped' in current_flow:
                G[src][dst]['SU'] = current_flow['speedUncapped']
            if 'speed' in current_flow:
                G[src][dst]['SC'] = current_flow['speed']


eps = 4e-5
for key, item in data_strava.items():
    if 'map' in item and 'polyline' in item['map']:
        points = item['map']['polyline']
        for i in range(1, len(points)):
            src = (points[i-1][1], points[i-1][0])
            dst = (points[i][1], points[i][0])
            dist1, src1 = KDTree.query([list(src)], k=1)
            dist2, dst1 = KDTree.query([list(dst)], k=1)
            if dist1 < eps:
                src = src1
            if dist2 < eps:
                dst = dst1
            if not dst in G[src]:
                dist = calculate_distance(src[0], src[1], dst[0], dst[1])
                G.add_edge(src, dst, weight=dist)
            if 'effort_count' in G[src][dst]:
                G[src][dst]['effort_count'] += item['effort_count'] if 'effort_count' in item else 0
            elif 'effort_count' in item:
                G[src][dst]['effort_count'] = item['effort_count']
            if 'hazardous' in item:
                G[src][dst]['hazardous'] = item['hazardous']
