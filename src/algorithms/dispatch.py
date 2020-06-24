from .shortest_path.johnson import Johnson
from .shortest_path.bellman_ford import BellmanFord
from .tarjan import Tarjan
from .shortest_path.dijkstra import Dijkstra
from collections import deque
from copy import deepcopy
from random import random
from .shortest_path.floyd_warshall import FloydWarshall


class Dispatch:

    @staticmethod
    def fast_dipsatch(network):
        # O(N^2 log N) time, O(N) extra space

        distance_matrix = [[] for x in range(network.length)]

        potential_function = FloydWarshall.merrick_floyd_warshall(network)

        if not potential_function:
            return False

        min_leaders = Dispatch._tarjan(network)

        list_of_leaders = set(min_leaders)

        dict_of_children = {}

        for idx, i in enumerate(min_leaders):
            if i in list_of_leaders:
                if i in dict_of_children:
                    dict_of_children[i].append(idx)
                else:
                    dict_of_children[i] = [idx]

        for src_idx in list_of_leaders:
            list_of_distances, predecessor_graph = Dijkstra.dijkstra(
                network, src_idx, potential_function=potential_function, path=True, list_of_leaders=list_of_leaders)

            #print(list_of_distances, predecessor_graph)

            # listy = [path from 3 to 0] = [3, 2, 1, 0]
            for listy in predecessor_graph:
                print(listy)
                intersecting_edges = []
                # get intersecting edges
                marked_edges = []
                for (src_idx, middle_idx), target_idx in intersecting_edges:
                    D_A_B = list_of_distances[src_idx][middle_idx] + \
                        list_of_distances[middle_idx][target_idx]
                    D_C = list_of_distances[src_idx][target_idx]
                    D_A = list_of_distances[src_idx][middle_idx]
                    D_C_B = list_of_distances[src_idx][target_idx] + \
                        list_of_distances[target_idx][middle_idx]
                    if D_A_B == D_C and D_A == D_C_B:
                        if (src_idx, target_idx) not in marked_edges and (src_idx, middle_idx) not in marked_edges:
                            if random() < 0.5:
                                marked_edges.append((src_idx, target_idx))
                            else:
                                marked_edges.append((src_idx, middle_idx))
                    else:
                        if D_A_B == D_C:
                            marked_edges.append((src_idx, target_idx))
                        if D_A == D_C_B:
                            marked_edges.append((src_idx, middle_idx))
                for node_idx, succ_idx in marked_edges:
                    if succ_idx in network.successor_edges[node_idx]:
                        network.delete_edge(node_idx, succ_idx)

        return network


    @ staticmethod
    def _tarjan(network):
        t = Tarjan(network)
        return t.tarjan()

    # @ staticmethod
    # def convert_to_dispatchable(network):
    #     # O(N^3) time, O(N^2) extra space
    #     if not network.dist_up_to_date:
    #         FloydWarshall.floyd_warshall(network)
    #     if not network.distance_matrix:
    #         return False
    #     distance_matrix = deepcopy(network.distance_matrix)
    #     marked_edges = []
    #     for u, distances in enumerate(network.distance_matrix):
    #         for v, delta in enumerate(distances):
    #             if u != v:
    #                 network.successor_edges[u][v] = delta
    #     intersecting_edges = Dispatch._get_intersecting_edges(network)
    #     # print(intersecting_edges)
    #     # print(distance_matrix)
    #     for (src_idx, middle_idx), target_idx in intersecting_edges:
    #         D_A_B = distance_matrix[src_idx][middle_idx] + \
    #             distance_matrix[middle_idx][target_idx]
    #         D_C = distance_matrix[src_idx][target_idx]
    #         D_A = distance_matrix[src_idx][middle_idx]
    #         D_C_B = distance_matrix[src_idx][target_idx] + \
    #             distance_matrix[target_idx][middle_idx]
    #         if D_A_B == D_C and D_A == D_C_B:
    #             if (src_idx, target_idx) not in marked_edges and (src_idx, middle_idx) not in marked_edges:
    #                     marked_edges.append((src_idx, target_idx))
    #         else:
    #             if D_A_B == D_C:
    #                 marked_edges.append((src_idx, target_idx))
    #             if D_A == D_C_B:
    #                 marked_edges.append((src_idx, middle_idx))
    #     # print(marked_edges)
    #     for node_idx, succ_idx in marked_edges:
    #         if succ_idx in network.successor_edges[node_idx]:
    #             network.delete_edge(node_idx, succ_idx)
    #
    #     return network
    #
    # @ staticmethod
    # def _get_intersecting_edges(network):
    #     num_tps = len(network.successor_edges)
    #     intersecting_edges = []
    #     arr = []
    #     for i in range(num_tps):
    #         for j in range(num_tps):
    #             if i == j:
    #                 continue
    #             for k in range(num_tps):
    #                 if k == i or k == j:
    #                     continue
    #                 if sorted([i, j]) in arr:
    #                     continue
    #                 arr.append(sorted([i, j]))
    #                 intersecting_edges.append(((i, j), k))
    #     return intersecting_edges
    #
    # @staticmethod
    # def _intersecting_edges(leader, child_array):
    #     intersecting_edges = []
    #     for i in child_array:
    #         for j in child_array:
    #             if i == j or i == leader or j == leader:
    #                 continue
    #             intersecting_edges.append(((leader, i), j))
    #     return intersecting_edges



    def convert_to_dispatchable(network):
        # O(N^3) time, O(N^2) extra space
        network.distance_matrix = FloydWarshall.merrick_floyd_warshall(network)
        if not network.distance_matrix:
            return False
        for u, distances in enumerate(network.distance_matrix):
            for v, delta in enumerate(distances):
                if u != v:
                    network.successor_edges[u][v] = delta
        marked_edges = Dispatch._get_marked_edges(network)
        for node_idx, succ_idx in marked_edges:
            if succ_idx in network.successor_edges[node_idx]:
                network.delete_edge(node_idx, succ_idx)
        return network



    @ staticmethod
    def _get_intersecting_edges(network):
        length = network.length
        intersecting_edges = []
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1, length):
                    yield (i,j,k)
                    yield (i,k,j)
                    yield (j,i,k)
                    yield (j,k,i)
                    yield (k,i,j)
                    yield (k,j,i)

    @staticmethod
    def _is_dominated(D_ac, D_ab, D_bc):
        return D_ac == D_ab + D_bc

    @staticmethod
    def _get_marked_edges(network):
        D = network.distance_matrix
        marked_edges = []
        for i,j,k in Dispatch._get_intersecting_edges(network):
            if D[i][j] >= 0 and D[i][k] >= 0:
                if Dispatch._is_dominated(D[i][k], D[i][j], D[j][k]):
                    if Dispatch._is_dominated(D[i][j], D[i][k], D[k][j]):
                        if not (i,j) in marked_edges and not (i,k) in marked_edges:
                            marked_edges.append((i,j))
                    else:
                        marked_edges.append((i,k))
                elif Dispatch._is_dominated(D[i][j], D[i][k], D[k][j]):
                    marked_edges.append((i,j))
            elif D[j][k] < 0:
                if Dispatch._is_dominated(D[i][k], D[k][j], D[j][i]):
                    if Dispatch._is_dominated(D[j][k], D[k][i], D[i][j]):
                        if not (i,k) in marked_edges and not (j,k) in marked_edges:
                            marked_edges.append((j,k))
                    else:
                        marked_edges.append((i,k))
                elif Dispatch._is_dominated(D[j][k], D[k][i], D[i][j]):
                    marked_edges.append((j,k))
        # for i, edges in enumerate(D):
        #     for j, delta in enumerate(edges):
        #         if delta == float("inf") and (i,j) not in marked_edges:
        #             marked_edges.append((i,j))
        return marked_edges
