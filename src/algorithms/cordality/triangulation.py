from ..shortest_path.johnson import Johnson

class Triangulation:
    """
    Class containing static methods relating to making the underlying graphs of STNs triangular
    """

    @staticmethod
    def naive(stn, ordering):
        if not stn.dist_up_to_date:
            stn.distance_matrix = Johnson.merrick_johnson(stn)
        if stn.distance_matrix:
            neighborhoods = [set() for x in range(stn.length)]
            stn.pred_edges_up_to_date = False
            new_edges = stn.successor_edges
            for u, edge_list in enumerate(stn.successor_edges):
                neighborhoods[u].update(edge_list.keys())
                for v in edge_list:
                    neighborhoods[v].add(u)
            for k in range(stn.length):
                v_k = ordering[k]
                for i in range(k):
                    v_i = ordering[i]
                    if v_i in neighborhoods[v_k]:
                        for j in range(k):
                            v_j = ordering[j]
                            if v_j in neighborhoods[v_k]:
                                if v_j not in stn.successor_edges[v_i]:
                                    new_edges[v_i][v_j] = stn.distance_matrix[v_i][v_j]
                                if v_i not in stn.successor_edges[v_j]:
                                    new_edges[v_j][v_i] = stn.distance_matrix[v_j][v_i]
            stn.successor_edges = new_edges
            return stn
        return False



    @staticmethod
    def TY(stn, ordering):
        """
        Creates a triangular graph for an stn with a percribed ordering using the Tarjan and Yannakakis algorithm
        ------------------------------------------------------------------
        Input:
            stn, the target STN
            ordering, the percribed ordering in the form of a list of ints

        Output:
            stn, the triangular stn

        Effects:
            destructively modifies the stn to be triangular
        ------------------------------------------------------------------
        """
        stn.pred_edges_up_to_date = False
        if not stn.dist_up_to_date:
            stn.distance_matrix = Johnson.merrick_johnson(stn)
        if stn.distance_matrix:
            new_edges = []
            seen = []
            follow = []
            for x in range(stn.length):
                new_edges.append(dict())
                seen.append(float("inf"))
                follow.append(False)
            for k in range(stn.length):
                v_k = ordering[k]
                seen[v_k] = k
                follow[v_k] = v_k
                for j in range(k+1, stn.length):
                    v_j = ordering[j]
                    if v_j in stn.successor_edges[v_k] or v_k in stn.successor_edges[v_j]:
                        v_i = v_j
                        while seen[v_i] > k:
                            new_edges[v_i][v_k] = stn.distance_matrix[v_i][v_k]
                            new_edges[v_k][v_i] = stn.distance_matrix[v_k][v_i]
                            seen[v_i] = k
                            v_i = follow[v_i]
                        if follow[v_i] == v_i:
                            follow[v_i] = v_k
            stn.successor_edges = new_edges
            return stn
        else:
            return False
