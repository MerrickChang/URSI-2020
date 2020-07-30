##===================================
##File: chleq.py
##Author: Merrick Chang
##Date: July 2019
##===================================

from ..path_consist.dpc import DirectedPathConsistency as DPC

class Chleq:
    """
    Static methods relating to the Chleq (1995) algorithm
    """

    @staticmethod
    def min_paths(stn, s, ordering):
        """
        Cleq (1995) algorithm for calculating the distance from a given source node to each other node
        --------------------------------------------------------------------------
        Input:
            stn, the target STN
            s, the source node
            ordering, an ordering for the vertices in the form of a list of ints,

        Output:
            D, the lists of distances from each vertex from the source
        --------------------------------------------------------------------------
        """
        D = [float('inf') for i in range(stn.length)]
        D[s] = 0
        for k in range(s, 0, -1):
            x_k = ordering[k]
            for j in range(k):
                x_j = ordering[j]
                if x_j in stn.successor_edges[x_k]:
                    D[x_j] = min(D[x_j], D[x_k] + stn.successor_edges[x_k][x_j])
        for k in range(stn.length):
            x_k = ordering[k]
            for j in range(k+1, stn.length):
                x_j = ordering[j]
                if x_j in stn.successor_edges[x_k]:
                    D[x_j] = min(D[x_j], D[x_k] + stn.successor_edges[x_k][x_j])
        return D

    @staticmethod
    def get_distance_matrix(stn, ordering):
        """
        The Chleq-ASAP algorithm for finding the distance distance_matrix
        ------------------------------------------------------------------
        Input:
            stn, the target STN
            ordering, an ordering for the vertices in the form of a list of ints

        Output:
            D, the distance matrix of the stn

        Effects:
            Destructively modifies the target stn to be DPC with respect to the ordering
        --------------------------------------------------------------------
        """
        if DPC.convert_to_DPC(stn, ordering):
            D = [[float('inf') for y in range(stn.length)] for x in range(stn.length)]
            for i in range(stn.length):
                D[i] = Chleq.min_paths(stn, i, ordering)
            return D
        else:
            return False
