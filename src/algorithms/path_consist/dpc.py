class DirectedPathConsistency:
    @staticmethod
    def convert_to_DPC(stn, ordering):
        stn.pred_edges_up_to_date = False
        for k in range(stn.length):
            x_k = ordering[k]
            for i in range(k):
                x_i = ordering[i]
                for j in range(k):
                    x_j = ordering[j]
                    if x_k in stn.successor_edges[x_i] and x_j in stn.successor_edges[x_k]:
                        alt = stn.successor_edges[x_i][x_k] + stn.successor_edges[x_k][x_j]
                        if x_j in stn.successor_edges[x_i]:
                            if alt < stn.successor_edges[x_i][x_j]:
                                stn.successor_edges[x_i][x_j] = alt
                        else:
                            stn.successor_edges[x_i][x_j] = alt
                    if x_k in stn.successor_edges[x_j] and x_i in stn.successor_edges[x_k]:
                        alt = stn.successor_edges[x_j][x_k] + stn.successor_edges[x_k][x_i]
                        if x_i in stn.successor_edges[x_j]:
                            if alt < stn.successor_edges[x_j][x_i]:
                                stn.successor_edges[x_j][x_i] = alt
                        else:
                            stn.successor_edges[x_j][x_i] = alt
        return stn
