from graph import Graph
from node import Node
from stn import STN
from stnu import STNU


class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.network = []

    def read_file(self):
        file = open(self.file_path, "r")
        state = ""
        for line in file:
            if "network" in line.lower():
                state = "NETWORK_TYPE"
                continue
            if state == "NETWORK_TYPE":
                if "u" not in line.lower():
                    self.network = STN()
                    return self.read_stn(file)
                elif "u" in line.lower():
                    self.network = STNU()
                    return self.read_stnu(file)
                else:
                    # throw an error
                    pass

    def read_stn(self, file):
        state = ""
        for line in file:
            if line.startswith('#'):
                if "points" in line.lower() and "num" in line.lower():
                    state = "NO_POINTS"
                elif "edges" in line.lower() and "num" in line.lower():
                    state = "NO_EDGES"
                elif "links" in line.lower():
                    state = "NO_LINKS"
                elif "names" in line.lower():
                    state = "NAMES"
                elif "edges" in line.lower():
                    state = "EDGES"
                elif "links" in line.lower():
                    state = "LINKS"
                else:
                    pass
            else:
                if state == 'NO_POINTS':
                    # for testing
                    no_points = int(line)
                    self.network.length = no_points
                    self.network.successor_edges = [
                        [] for i in range(no_points)]
                elif state == 'NO_EDGES':
                    # for testing
                    # no_edges = int(line)
                    pass
                elif state == 'NO_LINKS':
                    # for testing, throw an error
                    # no_links = int(line)
                    pass
                elif state == 'NAMES':
                    list_of_nodes = line.split()
                    for idx, node_name in enumerate(list_of_nodes):
                        # idx to node_name dict
                        self.network.names_dict[node_name] = idx
                elif state == 'EDGES':
                    weights = line.split()
                    # make a list of list of tuples
                    idxKey = self.network.names_dict[weights[0]]
                    idx_value = self.network.names_dict[weights[2]]
                    tup = (idx_value, weights[1])
                    self.network.successor_edges[idx].append(tup)
                elif state == 'LINKS':
                    # for testing, throw an error
                    pass
                else:
                    pass

    def read_stnu(self, file):
        state = ""
        for line in file:
            if line.startswith('#'):
                if "points" in line.lower() and "num" in line.lower():
                    state = "NO_POINTS"
                elif "edges" in line.lower() and "num" in line.lower():
                    state = "NO_EDGES"
                elif "links" in line.lower():
                    state = "NO_LINKS"
                elif "names" in line.lower():
                    state = "NAMES"
                elif "edges" in line.lower():
                    state = "EDGES"
                elif "links" in line.lower():
                    state = "LINKS"
                else:
                    pass
            else:
                if state == 'NO_POINTS':
                    # for testing
                    no_points = int(line)
                    self.netowrk.length = no_points
                    self.network.successor_edges = [
                        [] for i in range(no_points)]
                elif state == 'NO_EDGES':
                    # for testing
                    # no_edges = int(line)
                    pass
                elif state == 'NO_LINKS':
                    # for testing, throw an error
                    # no_links = int(line)
                    pass
                elif state == 'NAMES':
                    list_of_nodes = line.split()
                    for idx, node_name in enumerate(list_of_nodes):
                        # idx to node_name dict
                        self.network.names_dict[node_name] = idx
                elif state == 'EDGES':
                    weights = line.split()
                    # make a list of list of tuples
                    idx = self.network.names_dict[weights[0]]
                    idx_value = self.network.names_dict[weights[2]]
                    tup = (idx_value, weights[1])
                    self.network.successor_edges[idx].append(tup)
                elif state == 'LINKS':
                    # for testing, throw an error
                    pass
                else:
                    pass

