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
                    if x_i in stn.successor_edges[x_k] and x_j in stn.successor_edges[x_k]:
                        if not x_j in stn.successor_edges[x_i]:
                            stn.successor_edges[x_i][x_j] = float("inf")
                        if not x_i in stn.successor_edges[x_j]:
                            stn.successor_edges[x_j][x_i] = float("inf")
                    else:
                        if x_k in stn.successor_edges[x_i]:
                            if x_j in stn.successor_edges[x_k]:
                                alt = stn.successor_edges[x_i][x_k] + stn.successor_edges[x_k][x_j]
                                if x_j in stn.successor_edges[x_i]:
                                    if alt < stn.successor_edges[x_i][x_j]:
                                        stn.successor_edges[x_i][x_j] = alt
                                else:
                                    stn.successor_edges[x_i][x_j] = alt
                            elif x_k in stn.successor_edges[x_j] and not x_j in stn.successor_edges[x_i]:
                                stn.successor_edges[x_i][x_j] = float("inf")
                        if x_k in stn.successor_edges[x_j]:
                            if x_i in stn.successor_edges[x_k]:
                                alt = stn.successor_edges[x_j][x_k] + stn.successor_edges[x_k][x_i]
                                if x_i in stn.successor_edges[x_j]:
                                    if alt < stn.successor_edges[x_j][x_i]:
                                        stn.successor_edges[x_j][x_i] = alt
                                else:
                                    stn.successor_edges[x_j][x_i] = alt
                            elif x_k in stn.successor_edges[x_i] and not x_i in stn.successor_edges[x_j]:
                                stn.successor_edges[x_j][x_i] = float("inf")
        for u, edge_list in enumerate(stn.successor_edges):
            for v, delta in edge_list.items():
                if u in stn.successor_edges[v]:
                    if delta + stn.successor_edges[v][u] < 0:
                        return False
        return stn
