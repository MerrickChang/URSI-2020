##===================================
##File: solution_update.py
##Author: Merrick Chang
##Date: May 2020
##===================================

import heapq
import copy
class SolutionUpdate:
    def rsjm(stn, solution, constraint):
        """
        Implements incremental update method for STN solutions from G. Ramalingam et al. (1999).

        Effects:
             Adds the constraint if the the STN would remain feasible after its addition.
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
                        scaled_path_length = delta_x + solution[x] + delta_xy - solution[y]
                        for index, values in enumerate(min_heap):
                            path_length, z = values
                            if z==y and scaled_path_length < path_length:
                                min_heap.pop(index)
                                print(min_heap)
                                heapq.heappush(min_heap, (scaled_path_length, y))
                                break
        return S_prime
