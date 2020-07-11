from ..networks.stn import STN
from random import random, randrange, sample, randint, choice
import math
import heapq
from ..utils.probability import Probability


class RandomSTN:

    def random_stns(self, no_of_stns, max_no_of_nodes, max_weight=100, min_weight=-100, write_to_file = False):
        """
         random_stns: Generates and writes to files as many STNs as the user
                      wants.
         -------------------------------------------------------------
         INPUTS:  no_of_stns: An integer representing the number of STNs to be
                              generated
                  max_no_of_nodes: An integer representing the max no of nodes
                                   a STN generated can have
                  max_weight: An integer representing the max weight to be
                              assigned to any edge in a STN. Assigned a default
                              value of 100.
         OUTPUT:  networks: An array of STNs
         SIDE EFFECTS:  Writes the genrated STNs to individual files.
         --------------------------------------------------------------
         """
        networks = []
        for _ in range(no_of_stns):
            num = int(random() * max_no_of_nodes + 1)
            num = max(3, num)
            network = self.random_stn(num, max_weight, min_weight)
            networks.append(network)
        if write_to_file:
            for network in networks:
                self.write_stn(network, _)
        return networks




    def random_stn(self, no_of_nodes, max_weight=100, min_weight=-100, density_probability=None, node_names=None):
        """
         random_stn: Generates a random STN.
         -------------------------------------------------------------
         INPUTS:  no_of_nodes: An integer representing the number of nodes the
                  STN is going to have.
                  max_weight: An integer representing the max weight to be
                              assigned to any edge in the STN.
                  density_probability: A float representing the density of
                                       edges in the STN. Default value is None.
                  node_names: A list representing the node names of the STN.
                              Default value is None.
         OUTPUT:  network: A randomly genrated STN.
         --------------------------------------------------------------
         """
        network = STN()
        network.length = no_of_nodes
        if not node_names:
            node_names = [str(i) for i in range(network.length)]
        network.names_list = node_names
        for node_idx, node in enumerate(node_names):
            network.names_dict[node] = node_idx
        network.successor_edges = [{} for i in range(network.length)]
        self.random_edges(network, max_weight, min_weight, density_probability)
        return network





    def random_edges(self, network, max_weight=100, min_weight=-100, density_probability=None):
        """
         random_edges: Randomly populates the successor_edges of a randomly
                       generated STN.
         -------------------------------------------------------------
         INPUTS:  network: A randomly generated STN.
                  max_weight: An integer representing the max weight to be
                              assigned to any edge in the STN. Assigned a
                              default value of 100.
                  density_probability: A float representing the density of
                                       edges in the STN. Random if not given.
         OUTPUT:  None
         SIDE EFFECTS:  Randomly populates the successor_edges of a STN.
         --------------------------------------------------------------
         """
        if not density_probability or density_probability > 1 or type(density_probability) != float:
            density_probability = random()
        counter = 0
        for i in range(network.length):
            for j in range(network.length):
                rand = random()
                if rand < 0.5 * density_probability:
                    network.successor_edges[i][j] = int(
                        randrange(1, max_weight, 1))
                    counter += 1
                elif rand < density_probability and i!=j:
                    network.successor_edges[i][j] = int(
                        randrange(min_weight, -1, 1))
                    counter += 1
        if counter == 0:
            x = randrange(0, network.length, 1)
            r = list(range(network.length))
            r.pop(x)
            y = choice(r)
            network.successor_edges[x][y] = int(randrange(min_weight, -1, 1))




    def write_stn(self, network, stn_no):
        """
         write_stn: Writes a randomly generated STN to a file.
         -------------------------------------------------------------
         INPUTS:  network: A randomly generated STN.
                  stn_no: An integer representing a unique key for the STN to be
                          included in the file name.
         OUTPUT:  None
         SIDE EFFECTS:  Writes a randomly generated STN to a file.
         --------------------------------------------------------------
         """
        file = open('myfile' + str(stn_no) + '.txt', "w")
        edge_string = ""
        edge_counter = 0
        names_string = ""
        for name in network.names_list:
            names_string += name + " "
        for src_idx, dict in enumerate(network.successor_edges):
            for successor_idx, weight in dict.items():
                edge_string += str(network.names_list[src_idx]) + " " + str(
                    weight) + " " + str(network.names_list[successor_idx]) + "\n"
                edge_counter += 1
        L = ["# KIND OF NETWORK \n", "STN" + "\n", "# Num Time-Points \n",
             str(network.length) +
             "\n", "# Num Ordinary Edges \n", str(edge_counter) + "\n",
             "# Time-Point Names \n", names_string + "\n", "# Ordinary Edges \n", edge_string]
        file.writelines(L)

    # @staticmethod
    # def _diforest_prim(stn, sources, heap = False):
    #     """
    #     Implements a modified version of Prim's algorithm designed to assist with consistent STN generation
    #     """
    #     diforest_pred = dict()
    #     incident = set()
    #     if not heap:
    #         heap = [(delta, u, v) for u, v in edge_list for u, edge_list in enumerate(stn.successor_edges)]
    #     heapq.heapify(heap)
    #     while len(heap)!=0 and len(incident) < stn.length:
    #
    #     return diforest_pred

    @staticmethod
    def merrick_consistent_stn(min_no_of_nodes, max_no_of_nodes, edge_prob, min_weight, max_weight):
        """
        Randomly generates a consistent STN. A custom algorithm designed by Merrick Chang.
        ------------------------------------------------------------------

        Inputs:
            min_no_of_nodes, the minimum number of nodes that can be in the stn
            max_no_of_nodes, the maximum number of nodes that can be in the stn
            edge_prob, the probability that there is an edge between two arbitary nodes **in either direction**
            min_weight, the minimum allowed weight for an edge in the STN
            max_weight, the maximum allowed wieght for an edge in the STN

        Outputs:
            stn, an stn

        Effects:
            stn will be generated with predecessor_edges filled automatically
        -------------------------------------------------------------------
        """
        stn = STN()
        length = randint(min_no_of_nodes, max_no_of_nodes)
        stn.length = length
        degrees = []
        for index in range(length):
            stn.names_list.append(index)
            stn.names_dict[index] = index
            degrees.append(0)
        stn.update_predecessors()
        stn.successor_edges = [{} for x in range(length)]
        stn.pred_edges_up_to_date = True
        sources_w_pot = dict()
        #heap = []
        default_pot = [float("inf") for x in range(length)]
        for u in range(length-1):
            num_neg_outedges = Probability.binom_dist(length - u - 1, 2*edge_prob/3)
            ends = sample(list(range(u+1, length)), num_neg_outedges)
            if not u in stn.predecessor_edges:
                sources_w_pot[u] = default_pot.copy()
                sources_w_pot[u][u] = 0
                for v in ends:
                    delta = randint(min_weight, max_weight)
                    #heap.append((delta, u, v))
                    stn.predecessor_edges[v][u] = delta
                    stn.successor_edges[u][v] = delta
                    sources_w_pot[u][v] = delta
            else:
                 for v in ends:
                     delta = randint(min_weight, max_weight)
                     #heap.append((delta, u, v))
                     stn.predecessor_edges[v][u] = delta
                     stn.successor_edges[u][v] = delta
                     for pot in sources_w_pot.values():
                         alt = pot[u] + delta
                         if alt < pot[v]:
                             pot[v] = alt
        min_weight = max(min_weight, 0)
        #min_spanning_forrest = RandomSTN._diforest_prim(stn, sources, heap)
        for u in range(length-1, 0, -1):
            num_neg_outedges = Probability.binom_dist(u-1, edge_prob)
            ends = sample(range(u-1, -1, -1), num_neg_outedges)
            for v in ends:
                if not v in stn.successor_edges[u]:
                    min_weight_consistent = max([x[v] - x[u] for x in sources_w_pot.values()])
                    if min_weight_consistent <= max_weight:
                        delta = randint(max(min_weight, min_weight_consistent), max_weight)
                        stn.predecessor_edges[v][u] = delta
                        stn.successor_edges[u][v] = delta
                        for x in sources_w_pot.values():
                            alt = x[u] + delta
                            if alt < x[v]:
                                x[v] = alt
        return stn





    @staticmethod
    def generate_random_consistent_dgraph(n, min_dist, max_dist):
        dgraph = [[0 for x in range(len(n))] for x in range(n)]
        return dgraph
