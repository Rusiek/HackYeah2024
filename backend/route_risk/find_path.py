import pickle
import networkx as nx
from flask import Flask, request, jsonify
from sklearn.neighbors import KDTree

app = Flask(__name__)

CORS(app)

G = []

with open('backend/route_risk/nx_graph_00.pkl', 'rb') as f:
    G.append(pickle.load(f))

with open('backend/route_risk/nx_graph_01.pkl', 'rb') as f:
    G.append(pickle.load(f))

with open('backend/route_risk/nx_graph_10.pkl', 'rb') as f:
    G.append(pickle.load(f))

with open('backend/route_risk/nx_graph_11.pkl', 'rb') as f:
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

    start = kdTree.query([start])[1]
    end = kdTree.query([end])[1]
    start = (start[0][0], start[0][1])
    end = (end[0][0], end[0][1])
    
    mask = avoid * 2 + velo
    path = nx.shortest_path(G[mask], source=start, target=end, weight='weight')
    for i in range(len(path) - 1):
        path[i] = [list(path[i]), list(path[i + 1]), G[mask][path[i]][path[i + 1]]['risk']]

    return jsonify(path)

if __name__ == '__main__':
    app.run('127.0.0.1', 5005, debug=True)
