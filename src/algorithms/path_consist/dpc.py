##===================================
##File: dpc.py
##Author: Merrick Chang
##Date: July 2019
##===================================


class DirectedPathConsistency:
    @staticmethod
    def convert_to_DPC(stn, ordering): #TESTED!
        stn.pred_edges_up_to_date = False
        for k in range(stn.length):
            x_k = ordering[k]
            for i in range(k):
                x_i = ordering[i]
                for j in range(k):
                    x_j = ordering[j]
                    if not x_i in stn.successor_edges[x_k]:
                        stn.successor_edges[x_k][x_i] = float("inf")
                    if not x_j in stn.successor_edges[x_k]:
                        stn.successor_edges[x_k][x_j] = float("inf")
                    if not x_k in stn.successor_edges[x_i]:
                        stn.successor_edges[x_i][x_k] = float("inf")
                    if not x_k in stn.successor_edges[x_j]:
                        stn.successor_edges[x_j][x_k] = float("inf")
                    if x_i!= x_j:
                        if not x_j in stn.successor_edges[x_i]:
                            stn.successor_edges[x_i][x_j] = float("inf")
                        if not x_i in stn.successor_edges[x_j]:
                            stn.successor_edges[x_j][x_i] = float("inf")
                        alt = stn.successor_edges[x_i][x_k] + stn.successor_edges[x_k][x_j]
                        if alt < stn.successor_edges[x_i][x_j]:
                            stn.successor_edges[x_i][x_j] = alt

        for u, edge_list in enumerate(stn.successor_edges):
            for v, delta in edge_list.items():
                if u in stn.successor_edges[v]:
                    if delta + stn.successor_edges[v][u] < 0:
                        return False
        return stn
