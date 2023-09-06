import networkx as nx
import math

from utils.create_connected_graph import create_connected_graph

dict_route_costs = {"local": 1.0, "express": 2.0}

def test_create_connected_graph_empty_graph_passed_return_empty_graph(self):
    G = nx.Graph()
    connected_graph = create_connected_graph(G, dict_route_costs)

    self.assertEqual(len(connected_graph.edges), 0)

def test_create_connected_graph_single_node_graph_passed_return_empty_graph(self):
    G = nx.Graph()
    G.add_node(1, pos=(0, 0), building_type="factory")
    connected_graph = create_connected_graph(G, dict_route_costs)

    self.assertEqual(len(connected_graph.edges), 0)

def test_create_connected_graph_two_factories_graph_passed_return_graph_one_local_route(self):
    G = nx.Graph()
    G.add_node(1, pos=(0, 0), building_type="factory")
    G.add_node(2, pos=(0, 1), building_type="factory")

    x1, y1 = G.nodes[1]['pos']
    x2, y2 = G.nodes[2]['pos']

    euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    expected_edge_weight = euclidean_distance * dict_route_costs["local"]

    connected_graph = create_connected_graph(G, dict_route_costs)

    self.assertEqual(len(connected_graph.edges), 1)
    self.assertEqual(connected_graph[1][2]['route'], 'local') # Check route type
    self.assertEqual(connected_graph[1][2]['weight'], expected_edge_weight) # Check edge weight

def test_create_connected_graph_two_warehouses_graph_passed_return_graph_one_express_route(self):
    G = nx.Graph()
    G.add_node(1, pos=(0, 0), building_type="warehouse")
    G.add_node(2, pos=(0, 1), building_type="warehouse")

    x1, y1 = G.nodes[1]['pos']
    x2, y2 = G.nodes[2]['pos']

    euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    expected_edge_weight = euclidean_distance * dict_route_costs["local"]

    connected_graph = create_connected_graph(G, dict_route_costs)
    self.assertEqual(len(connected_graph.edges), 1)
    self.assertEqual(connected_graph[1][2]['route'], 'express') # Check route type
    self.assertEqual(connected_graph[1][2]['weight'], expected_edge_weight) # Check edge weight
    

def test_mixed_nodes(self):
    G = nx.Graph()
    G.add_node(1, pos=(0, 0), building_type="factory")
    G.add_node(2, pos=(0, 1), building_type="warehouse")
    G.add_node(3, pos=(1, 1), building_type="distribution_center")

    result = create_connected_graph(G, costs)
    self.assertEqual(len(result.edges), 2)
    self.assertEqual(result[2][3]['route'], 'express')
    self.assertEqual(result[1][2]['route'], 'local')