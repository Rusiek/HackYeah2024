import numpy as np
import networkit as nk
import networkx as nx
from datetime import datetime
from route_risk import RouteRisk
from model import RouteRiskBayesNet
from sklearn.neighbors import KDTree
from tqdm import tqdm
import json
import pickle

with open('backend/server/app/routes/cars/data/traffic_data.json') as f:
    data_here = json.load(f)

verticies = []
results = data_here.get('results')
idx = 1
for e in tqdm(results):
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

for i in tqdm(range(1, len(verticies))):
    if calculate_distance(verticies[i][1], verticies[i][0], verticies[i-1][1], verticies[i-1][0]) > eps:
        unique_verticies.append(verticies[i])

# print(len(unique_verticies))
KDTree = KDTree(unique_verticies)

with open('strava/segments_info2.json') as f2:
    data_strava = json.load(f2)

eps = 4e-5
for key, item in tqdm(data_strava.items()):
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

for e in tqdm(results):
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
for key, item in tqdm(data_strava.items()):
    if 'map' in item and 'polyline' in item['map']:
        points = item['map']['polyline']
        for i in range(1, len(points)):
            src = (points[i-1][1], points[i-1][0])
            dst = (points[i][1], points[i][0])
            dist1, src1 = KDTree.query([list(src)], k=1)
            dist2, dst1 = KDTree.query([list(dst)], k=1)
            
            # Convert src1 and dst1 (index arrays) into integers, then retrieve the corresponding coordinates
            src_idx = src1[0][0]  # Get the index for the nearest point to src
            dst_idx = dst1[0][0]  # Get the index for the nearest point to dst
            
            # Now use those indices to get the coordinates from the original KDTree data
            src = tuple(KDTree.data[src_idx])
            dst = tuple(KDTree.data[dst_idx])
            
            if not dst in G[src]:
                dist = calculate_distance(src[0], src[1], dst[0], dst[1])
                G.add_edge(src, dst, weight=dist)
            if 'effort_count' in G[src][dst]:
                G[src][dst]['effort_count'] += item.get('effort_count', 0)
            elif 'effort_count' in item:
                G[src][dst]['effort_count'] = item['effort_count']
            if 'hazardous' in item:
                G[src][dst]['hazardous'] = item['hazardous']


strava_hazardous_list = []
strava_effort_count_list = []
here_jam_factor_list = []
here_flow_speed_list = []
here_speed_cap_list = []

for edge in tqdm(G.edges(data=True)):
    src, dst, edge_data = edge
    strava_hazardous_list.append(edge_data.get('hazardous', None))
    strava_effort_count_list.append(edge_data.get('effort_count', None))
    here_jam_factor_list.append(edge_data.get('JF', None))
    here_flow_speed_list.append(edge_data.get('SU', None))
    here_speed_cap_list.append(edge_data.get('SC', None))

strava_hazardous_list = [x for x in strava_hazardous_list if x is not None]
strava_effort_count_list = [x for x in strava_effort_count_list if x is not None]
here_jam_factor_list = [x for x in here_jam_factor_list if x is not None]
here_flow_speed_list = [x for x in here_flow_speed_list if x is not None]
here_speed_cap_list = [x for x in here_speed_cap_list if x is not None]

print(strava_hazardous_list[:20])
print(strava_effort_count_list[:20])
print(here_jam_factor_list[:20])
print(here_flow_speed_list[:20])
print(here_speed_cap_list[:20])

model = RouteRisk(
    strava_popularity_list=strava_effort_count_list,
    strava_hazardous_list=strava_hazardous_list,
    here_jam_factor_list=here_jam_factor_list,
    here_flow_speed_list=here_flow_speed_list,
    here_speed_cap_list=here_speed_cap_list,
    model_path='backend/route_risk/BicycleModel.net'
)

for idx, edge in tqdm(enumerate(G.edges(data=True))):
    src, dst, edge_data = edge
    strava_effort_count = edge_data.get('effort_count', None)
    strava_hazardous = edge_data.get('hazardous', None)
    here_jam_factor = edge_data.get('JF', None)
    here_flow_speed = edge_data.get('SU', None)
    here_speed_cap = edge_data.get('SC', None)

    bn_data = model(
        strava_popularity=strava_effort_count,
        strava_hazardous=strava_hazardous,
        here_jam_factor=here_jam_factor,
        here_flow_speed=here_flow_speed,
        here_speed_cap=here_speed_cap
    )

    G[src][dst]['risk'] = bn_data['risk']
    if idx == 1000:
        break

def nx_to_nk_with_attributes(nx_graph: nx.Graph) -> nk.Graph:
    nk_graph_00 = nk.Graph(nx_graph.number_of_nodes(), weighted=True)
    nk_graph_01 = nk.Graph(nx_graph.number_of_nodes(), weighted=True)
    nk_graph_10 = nk.Graph(nx_graph.number_of_nodes(), weighted=True)
    nk_graph_11 = nk.Graph(nx_graph.number_of_nodes(), weighted=True)

    node_mapping = {node: idx for idx, node in enumerate(nx_graph.nodes())}

    for u, v, data in tqdm(nx_graph.edges(data=True)):
        nk_u = node_mapping[u]
        nk_v = node_mapping[v]
        weight_00 = data.get('weight', 1.0)
        weight_01 = weight_00 * (2 if data.get('risk', 'mid') == 'hi' else 1)
        weight_01 = weight_01 * (0.5 if data.get('risk', 'mid') == 'lo' else 1)
        weight_10 = weight_00 * (0.3 if data.get('velo', False) else 1)
        weight_11 = weight_01 * weight_10 / weight_00

        nk_graph_00.addEdge(nk_u, nk_v, weight_00)
        nk_graph_01.addEdge(nk_u, nk_v, weight_01)
        nk_graph_10.addEdge(nk_u, nk_v, weight_10)
        nk_graph_11.addEdge(nk_u, nk_v, weight_11)

    return nk_graph_00, nk_graph_01, nk_graph_10, nk_graph_11

nk_graph_00, nk_graph_01, nk_graph_10, nk_graph_11 = nx_to_nk_with_attributes(G)

with open('backend/route_risk/nk_graph_00.pkl', 'wb') as f:
    pickle.dump(nk_graph_00, f)

with open('backend/route_risk/nk_graph_01.pkl', 'wb') as f:
    pickle.dump(nk_graph_01, f)

with open('backend/route_risk/nk_graph_10.pkl', 'wb') as f:
    pickle.dump(nk_graph_10, f)

with open('backend/route_risk/nk_graph_11.pkl', 'wb') as f:
    pickle.dump(nk_graph_11, f)


# print(G.edges(data=True))
