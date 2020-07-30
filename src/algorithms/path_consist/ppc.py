##===================================
##File: ppc.py
##Author: Merrick Chang
##Date: July 2019
##===================================


from .dpc import DirectedPathConsistency

class PartialPathConsistency:
    @staticmethod
    def convert_to_PPC(stn): #UNTESTED!
        """
        Takes a cordal (consistent) STN and outputs a partially path consistent STN
        ---------------------------------------------------------------
        Input:
            stn, the target STN

        Output:
            stn, the PPC converted STN

        Effects:
            Destructively modifies stn to path consistent form
        """
        stn.pred_edges_up_to_date = False
        queue = []
        for u, edge_list in enumerate(stn.successor_edges):
            for v, delta in edge_list.items():
                queue.append((u,v))
        while len(queue) != 0:
            u,v = queue.pop()
            for x in range(stn.length):
                if v in stn.successor_edges[u]:
                    if x in stn.successor_edges[v]:
                        alt = stn.successor_edges[u][v] + stn.successor_edges[v][x]
                        if x in stn.successor_edges[u]:
                            if alt < stn.successor_edges[u][x]:
                                stn.successor_edges[u][x] = alt
                                queue.append((v,x))
                        else:
                            stn.successor_edges[u][x] = alt
                            queue.append((v,x))
        return stn

    @staticmethod
    def P3C(stn, ordering): #UNTESTED!
        """
        Implements P3C algorithm for partial path consistency from Planken (2013)
        ------------------------------------------------------------------------
        Input:
            stn, the target STN
            ordering, an ordering for the stn vertices in the form of a list of ints

        Output:
            stn, the PPC converted STN

        Effects:
            Destructively modifies stn to path consistent form
        ----------------------------------------------------------------------------
        """
        if DirectedPathConsistency.convert_to_DPC(stn, ordering):
            for k in range(stn.length):
                x_k = ordering[k]
                for i in range(k):
                    x_i = ordering[i]
                    for j in range(k):
                        x_j = ordering[j]
                        if x_j in stn.successor_edges[x_i]:
                            if x_k in stn.successor_edges[x_j] and x_k in stn.successor_edges[x_i]:
                                stn.successor_edges[x_i][x_k] = min(stn.successor_edges[x_i][x_k], stn.successor_edges[x_i][x_j] + stn.successor_edges[x_j][x_k])
                            if x_j in stn.successor_edges[x_k] and x_i in stn.successor_edges[x_k]:
                                stn.successor_edges[x_k][x_j] = min(stn.successor_edges[x_k][x_j], stn.successor_edges[x_k][x_i] + stn.successor_edges[x_i][x_j])
            return stn
        else:
            return False
