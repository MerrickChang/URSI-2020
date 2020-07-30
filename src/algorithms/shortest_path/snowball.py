##===================================
##File: snowball.py
##Author: Merrick Chang
##Date: July 2019
##===================================

from ..path_consist.dpc import DirectedPathConsistency

class Snowball:
    """
    Static methods relating to the Planken (2013) algorithm Snowball
    """
    @staticmethod
    def snowball(stn, ordering): #UNTESTED!
        """
        Planken (2013) method Snowball for calculating the distance matrix of a given STN
        ---------------------------------------------------------------------------------
        Input:
            stn, the target STN
            ordering, an ordering for the vertices in the form of a list of ints

        Output:
            D, the distance matrix of the target STNs

        Effects:
            Destructively modifies stn to be directed path consistent along the ordering
        ---------------------------------------------------------------------------------
        """
        if DirectedPathConsistency.convert_to_DPC(stn, ordering):
            D = [[float('inf') for y in range(stn.length)] for x in range(stn.length)]
            for i in range(stn.length):
                D[i][i] = 0
            for k in range(stn.length):
                x_k = ordering[k]
                for j in range(k):
                    x_j = ordering[j]
                    if x_k in stn.successor_edges[x_j]:
                        if x_j in stn.successor_edges[x_k]:
                            for i in range(k):
                                x_i = ordering[i]
                                D[x_i][x_k] = min(D[x_i][x_k], D[x_i][x_j] + stn.successor_edges[x_j][x_k])
                                D[x_k][x_i] = min(D[x_k][x_i], stn.successor_edges[x_k][x_j] + D[x_j][x_i])
                        else:
                            for i in range(k):
                                x_i = ordering[i]
                                D[x_i][x_k] = min(D[x_i][x_k], D[x_i][x_j] + stn.successor_edges[x_j][x_k])
                    elif x_j in stn.successor_edges[x_k]:
                        for i in range(k):
                            x_i = ordering[i]
                            D[x_k][x_i] = min(D[x_k][x_i], stn.successor_edges[x_k][x_j] + D[x_j][x_i])
            return D
        else:
            return False
