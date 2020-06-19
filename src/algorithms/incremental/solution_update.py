##===================================
##File: solution_update.py
##Author: Merrick Chang
##Date: June 2020
##===================================

import heapq
import copy
class SolutionUpdate:
    @staticmethod
    def _adjust_heap(min_heap, y, scaled_path_length):
        """
        A helper method to assist RSJM. The method conducts a greedy search on the heap for the inputed vertex.
        The method then modifies min_heap as required.
        ----------------------------------------------------------------------------------------------------------
        Input:
            min_heap, the heap being adjusted
            y, the target vertex
            scaled_path_length, the new path length after the addition of the new constraint

        Output:
            heap_changed, a variable that is True if the heap was modified and False if it wasn't.

        Effects:
            If a vertex is found and its weight is less than scaled_path_length, updates its weight to be scaled_path_length
            If the vertex is not in the heep, it is inserted into the heapq with weight scaled_path_length
        ----------------------------------------------------------------------------------------------------------
        """
        for index, values in enumerate(min_heap):
            path_length, z = values
            if z==y:
                if scaled_path_length < path_length:
                    min_heap.pop(index)
                    heapq.heappush(min_heap, (scaled_path_length, y))
                    return True
                else:
                    return False
        heapq.heappush(min_heap, (scaled_path_length, y))
        return True




    def rsjm(stn, solution, constraint):
        """
        Implements incremental update method for STN solutions from G. Ramalingam et al. (1999).
        -------------------------------------------------------------------------------------------
        Inputs:
            stn, the stn being updated
            solution, the solution being updated
            constraint, the new constraint

        Outputs:
            S_prime, which is an updated solution if the system is feasible if when the contraints is
                     added and False if the system is infeasible with the constraint

        Effects:
             Adds the constraint if the the STN would remain feasible after its addition.
        -------------------------------------------------------------------------------------------
        """
        u,v,delta = constraint
        stn.successor_edges[u][v] = delta
        S_prime = copy.deepcopy(solution)
        min_heap = []
        heapq.heappush(min_heap, (0, v))
        while len(min_heap) != 0:
            delta_x, x = heapq.heappop(min_heap)
            var = solution[u] + delta + solution[x] + delta_x - solution[v]
            if var < solution[x]:
                if x == u:
                    stn.successor_edges[u].pop(v)
                    return False
                else:
                    S_prime[x] = var
                    for y, delta_xy in stn.successor_edges[x].items():
                        SolutionUpdate._adjust_heap(min_heap, y, delta_x + solution[x] + delta_xy - solution[y])
        return S_prime
