import pickle
import time

import networkx as nx
from flask import Flask, request, jsonify
from sklearn.neighbors import KDTree
from flask_cors import CORS
import os

from graph import update

app = Flask(__name__)

CORS(app)

G = []

update()

with open(os.path.join(os.path.dirname(__file__), 'nx_graph_00.pkl'), 'rb') as f:
    G.append(pickle.load(f))

with open(os.path.join(os.path.dirname(__file__), 'nx_graph_01.pkl'), 'rb') as f:
    G.append(pickle.load(f))

with open(os.path.join(os.path.dirname(__file__), 'nx_graph_10.pkl'), 'rb') as f:
    G.append(pickle.load(f))

with open(os.path.join(os.path.dirname(__file__), 'nx_graph_11.pkl'), 'rb') as f:
    G.append(pickle.load(f))

nodes = list(G[0].nodes())
kdTree = KDTree(nodes)
# Endpoint do przetwarzania zapytań na danych
@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.json
    start = data['start']
    end = data['end']
    avoid = data['avoidUnsafe']
    velo = data['preferVelo']

    # print(start, end, avoid, velo)
    dist1, src = kdTree.query([start], k=1)
    dist2, dst = kdTree.query([end], k=1)
    src_idx = src[0][0]
    dst_idx = dst[0][0]
    start = tuple(kdTree.data[src_idx])
    end = tuple(kdTree.data[dst_idx])
    
    mask = avoid * 2 + velo
    path = nx.astar_path(G[mask], source=start, target=end, weight='weight')
    for i in range(len(path) - 1):
        response_dict = {}
        response_dict['path'] = [list(path[i]), list(path[i + 1])]
        response_dict['risk'] = G[mask][path[i]][path[i + 1]]['risk']
        path[i] = response_dict

    return jsonify(path)

@app.route('/get_edges', methods=['GET'])
def get_edges():
    edges = []
    for e in G[0].edges(data = True):
        response_dict = {}
        response_dict['path'] = [list(e[0]), list(e[1])]
        response_dict['risk'] = e[2]['risk']
        edges.append(response_dict)
    return jsonify(edges)

def actualize_traffic():
    while True:
        time.sleep(600)
        G = []
        update()
        with open(os.path.join(os.path.dirname(__file__), 'nx_graph_00.pkl'), 'rb') as f:
            G.append(pickle.load(f))

        with open(os.path.join(os.path.dirname(__file__), 'nx_graph_01.pkl'), 'rb') as f:
            G.append(pickle.load(f))

        with open(os.path.join(os.path.dirname(__file__), 'nx_graph_10.pkl'), 'rb') as f:
            G.append(pickle.load(f))

        with open(os.path.join(os.path.dirname(__file__), 'nx_graph_11.pkl'), 'rb') as f:
            G.append(pickle.load(f))

if __name__ == '__main__':
    app.run('127.0.0.1', 5005, debug=True)
    actualize_traffic()
