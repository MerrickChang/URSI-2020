##===================================
##File: potetnial.py
##Author: Merrick Chang
##Date: July 2019
##===================================

from ..incremental.solution_update import SolutionUpdate
from ...networks.stn import STN
import copy

class Potential:
    """
    Contains static methods relating to calculating the shortest path.
    """

    @staticmethod
    def hunsberger_posenato(stn):
        """
        Uses incremental potential updating method by Hunsberger and Posenato
        to calcluate shortest paths.
        """
        dist = [0 for x in range(stn.length)]
        stn_copy = STN()
        if not stn.pred_edges_up_to_date:
            stn.update_predecessors()
        stn_copy.predecessor_edges = [{} for x in range(stn.length)]
        stn_copy.pred_edges_up_to_date = True
        for X, edges in enumerate(stn.predecessor_edges):
            stn_copy.predecessor_edges[X] = edges
            dist = SolutionUpdate.update_potential(stn_copy, A = X, h = dist)
        return dist
