##===================================
##File: matrix_update.py
##Author: Merrick Chang
##Date: June 2020
##===================================

import copy

class DistanceMatrixUpdate:
    """
    The DistanceMatrixUpdate class contains static methods associated with incrementally updating the distance matrix for an STN.
    """

    @staticmethod
    def _get_predecessor_edges(succ, node_index):
        """
        Generator that finds precedessor edges of a given node

        --------------------------------------------------------------------------------------------------

        Inputs:
            succ, the list of sucessor edges
            node_index, index of the target node

        Outputs:
            edge, a tuple containing the start node of the edge and the weight of the edge

        --------------------------------------------------------------------------------------------------
        """
        for u, edge_list in enumerate(succ[:node_index]):
            for v, delta in edge_list.items():
                if v == node_index:
                    yield (u, delta)
        for u, edge_list in enumerate(succ[node_index+1:], start=node_index+1):
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
                            DistanceMatrixUpdate._prop_fwd(D_prime, t_z, t_i, t_j, affected, encountered, delta, succ, pred)



    @staticmethod
    def _prop_bwk(D_prime, t_s, t_v, t_i, encountered, succ, pred):
        for t_r, delta_rs in pred[t_s].items():
            if not t_r in encountered:
                encountered.add(t_r)
                D_rv = D_prime[t_r][t_v]
                var_1 = delta_rs + D_prime[t_s][t_i]
                if var_1 == D_prime[t_r][t_i]:
                    var_2 = var_1 + D_prime[t_i][t_v]
                    if var_2 <= D_rv:
                        try:
                            pred[t_v].pop(t_r)
                            succ[t_r].pop(t_v)
                        except KeyError:
                            pass
                        if var_2 < D_rv:
                            D_prime[t_r][t_v] = var_2
                            DistanceMatrixUpdate._prop_bwk(D_prime, t_r, t_v, t_i, encountered, succ, pred)




    @staticmethod
    def _pop_dominated_constraints(succ, pred, D, constraint):
        marked = []
        for i, edge_list in enumerate(succ):
            for j, delta in edge_list.items():
                if D[i][j] > delta:
                    continue
                elif D[i][j] == delta:
                    enum = dict(enumerate(D[i]))
                    enum.pop(i)
                    enum.pop(j)
                    for k, D_ik in enum.items():
                        if D[i][k]+D[k][j] == delta:
                            marked.append((i,j))
                            break
                    continue
                else:
                    marked.append((i,j))
        for i,j in marked:
            succ[i].pop(j)
            pred[j].pop(i)




    @staticmethod
    def _find_rigidities(D, i, succ, pred, rigidity = set()):
        for j, delta in succ[i].items():
            if delta == -D[j][i] and not j in rigidity:
                rigidity.add(j)
                rigidity.add(i)
                rigidity = IncrementalAlgorithm._find_rigidities(D, j, succ, pred, rigidity)
        for j, delta in pred[i].items():
            if delta == -D[i][j] and not j in rigidity:
                rigidity.add(j)
                rigidity.add(i)
                rigidity = IncrementalAlgorithm._find_rigidities(D, j, succ, pred, rigidity)
        return rigidity




    @staticmethod
    def _prop3_1(D_prime, t_i, t_j, delta, succ, pred):
        DistanceMatrixUpdate._pop_dominated_constraints(succ, pred, D_prime, (t_i, t_j, delta))
        D_prime[t_i][t_j] = delta
        affected = {t_j}
        DistanceMatrixUpdate._prop_fwd(D_prime, t_j, t_i, t_j, affected, set(), delta, succ, pred)
        for t_v in affected:
            DistanceMatrixUpdate._prop_bwk(D_prime, t_i, t_v, t_i, set(), succ, pred)
        return D_prime




    @staticmethod
    def _prop3_2(D_prime, t_i, t_j, delta, succ, pred):
        print("Ugh")
        return _prop3_1(D_prime, t_i, t_j, delta, succ, pred)



    @staticmethod
    def propagation(stn, distance_matrix, constraint, destructive = False):
        """
        Implements a propogating distance matrix updating algorithm

        --------------------------------------------------------------------------------------------------
        Inputs:
            stn, the target stn
            distance_matrix, 2-D array representing the distance matrix of the target
            constraint, the new constraint
            destructive, a boolean representing whether or not the inputed distance matrix should be overwritten.

        Outputs:
            D_prime, the new distance matrix
        --------------------------------------------------------------------------------------------------
        """
        t_i,t_j,delta = constraint
        D_prime = distance_matrix if destructive else copy.deepcopy(distance_matrix)
        succ = copy.deepcopy(stn.successor_edges)
        pred = [dict([(q, delta)
                for q, delta  in DistanceMatrixUpdate._get_predecessor_edges(succ, r)])
                for r in range(stn.length)]
        if type(t_i) == str:
            t_i, t_j = stn.names_dict[start], stn.names_dict[stop]
        if delta > -distance_matrix[t_j][t_i]:
            return DistanceMatrixUpdate._prop3_1(D_prime, t_i, t_j, delta, succ, pred)
        else:
            return DistanceMatrixUpdate._prop3_2(D_prime, t_i, t_j, delta, succ, pred)




    @staticmethod
    def naive(stn, distance_matrix, constraint, destructive = False):
        """
        Implements a naive distance matrix updating algorithm

        --------------------------------------------------------------------------------------------------
        Inputs:
            stn, the target stn
            distance_matrix, 2-D array representing the distance matrix of the target
            constraint, the new constraint
            destructive, a boolean representing whether or not the inputed distance matrix should be overwritten.

        Outputs:
            D_prime, the new distance matrix
        --------------------------------------------------------------------------------------------------
        """
        t_i,t_j,delta = constraint
        D_prime = distance_matrix if destructive else copy.deepcopy(distance_matrix)
        D_j = D_prime[t_j]
        for t_r, row in enumerate(D_prime):
            D_ri = row[t_i]
            for t_s, D_rs in enumerate(row):
                alt = D_ri+delta+D_j[t_s]
                if alt < D_rs:
                    D_prime[t_r][t_s] = alt
        return D_prime
