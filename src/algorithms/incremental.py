import copy

class IncrementalAlgorithms:
    
    @staticmethod
    def _get_precessor_edges(stn, node_index):
        """
        Generator that finds precedessor edges of a given node

        --------------------------------------------------------------------------------------------------

        Inputs:
            stn, the target stn
            node_index, index of the target node

        Outputs:
            edge, a tuple containing the start node of the edge and the weight of the edge

        --------------------------------------------------------------------------------------------------
        """
        for u, edge_list in enumerate(stn.successor_edges[:node_index]):
            for v, delta in edge_list.items():
                if v == node_index:
                    yield (u, delta)
        for u, edge_list in enumerate(stn.successor_edges[node_index+1:], start=node_index+1):
            for v, delta in edge_list.items():
                if v == node_index:
                    yield (u, delta)



    @staticmethod
    def _prop_fwd(D_prime, t_y, t_i, t_j, affected, encountered, delta, succ, pred):
        for t_z, delta_yz in succ[t_y].items():
            if not t_z in encountered:
                encountered.add(t_z)
                D_iz = D_prime[t_i][t_z]
                var_1 = D_prime[t_j][t_y] + delta_yz
                if var_1 == D_prime[t_j][t_z]:
                    var_2 = delta + var_1
                    if var_2 <= D_iz:
                        try:
                            succ[t_i].pop(t_z)
                            pred[t_z].pop(t_i)
                        except KeyError:
                            pass
                        if var_2 < D_iz:
                            D_prime[t_i][t_z] = var_2
                            affected.add(t_z)
                            IncrementalAlgorithms._prop_fwd(D_prime, t_z, t_i, t_j, affected, encountered, delta, succ, pred)
                    

    
    @staticmethod
    def _prop_bwk(D_prime, t_s, t_v, t_i, encountered, succ, pred):
        for t_r, delta_rs in pred[t_s].items():
            if t_r in encountered:
                encountered.add(t_r)
                D_rv = D_prime[t_r][t_v]
                var_1 = delta_rs + D_prime[t_s][t_i]
                if var_1 == D_prime[t_r][t_i]:
                    var_2 = var_1 + D[t_i][t_v]
                    if var_2 <= D_rv:
                        pred[t_v].pop(t_r)
                        succs[t_r].pop(t_v)
                        if var_2 < D_rv:
                            D_prime[t_r][t_v] = var_2
                            IncrementalAlgorithms._prop_bwk(D_prime, t_r, t_v, t_i, encountered, succ, pred)



    @staticmethod
    def propagation(stn, distance_matrix, constraint):
        """
        Implements the distance matrix updating algorithm
        Note: This method makes intensive use of deepcopy to make it faster. May strain memory for very large STNs.

        --------------------------------------------------------------------------------------------------
        Inputs:
            stn, the target stn
            distance_matrix, 2-D array representing the distance matrix of the target 
            constrain, the new constraint

        Outputs:
            D_prime, the new distance matrix
        --------------------------------------------------------------------------------------------------
        """
        
        t_i,t_j,delta = constraint
        if type(t_i) == str:
            t_i, t_j = stn.names_dict[start], stn.names_dict[stop]
        D_prime = copy.deepcopy(distance_matrix)
##        if -D_prime[t_j][t_i] <= delta and delta < D_prime[t_i][t_j]:
##            print("No need to update")
##            return D_prime
        succ = copy.deepcopy(stn.successor_edges)
        pred = [dict([(q, delta)
                for q, delta  in IncrementalAlgorithms._get_precessor_edges(stn, r)])
                for r in range(stn.length)]
        D_prime[t_i][t_j] = delta
        affected = {t_j}
        IncrementalAlgorithms._prop_fwd(D_prime, t_j, t_i, t_j, affected, set(), delta, succ, pred)
        for t_v in affected:
            IncrementalAlgorithms._prop_bwk(D_prime, t_i, t_v, t_i, set(), succ, pred)
        return D_prime
