from ..shortest_path.johnson import Johnson

class Triangulation:
    @staticmethod
    def naive(stn, ordering):
        pass

    def TY(stn, ordering):
        stn.pred_edges_up_to_date = False
        if not stn.dist_up_to_date:
            stn.distance_matrix = Johnson.merrick_johnson(stn)
        new_edges = []
        seen = []
        follow = []
        for x in range(stn.length):
            new_edges.append(dict())
            seen.append(-1)
            follow.append(False)
        for k in range(stn.length):
            v_k = ordering[k]
            seen[v_k] = k
            follow[v_k] = v_k
            for j in range(k+1, stn.length):
                v_j = ordering[j]
                v_i = v_j
                while seen[v_i] > k:
                    new_edges[v_i][v_k] = distance_matrix[v_i][v_k]
                    seen[v_i] = k
                    v_i = follow[v_i]
                if follow[v_i] = v_i:
                    follow[v_i] = v_k
        stn.successor_edges = new_edges
        return stn
