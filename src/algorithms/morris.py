import heapq
import copy


class MorrisConsistencyCheck:
    """
    Class containing static methods pertaining to a modified version of Morris (2014).
    Determines whether or not a given STN is consistent or not.
    """
    @staticmethod
    def is_consistent(stn):
        if not stn.pred_edges_up_to_date:
            stn.update_predecessors()
        terminated = set()
        for node, edges in enumerate(stn.predecessor_edges):
            if MorrisConsistencyCheck._is_negative_node(stn, node):
                dup = copy.deepcopy(stn)
                if not MorrisConsistencyCheck._prop_bwk(dup, node, terminated):
                    return False
        return True


    @staticmethod
    def _prop_bwk(stn, src, terminated = set(), ancestors = set()):
        if src in ancestors: #if ancestor call with same source
            return False
        if src in terminated: #prior terminated call with source
            return True
        dist = [float("inf") for x in range(stn.length)]
        dist[src] = 0
        queue = []
        heapq.heapify(queue)
        for start, delta in stn.predecessor_edges[src].items():
            heapq.heappush(queue, (delta, start))
            dist[start] = delta
        while len(queue) != 0:
            delta, u = heapq.heappop(queue)
            if dist[u] >= 0:
                stn.successor_edges[u][src] = dist[u]
                stn.predecessor_edges[src][u] = dist[u]
                continue
            if MorrisConsistencyCheck._is_negative_node(stn, u):
                new_call_ancestors = copy.deepcopy(ancestors)
                new_call_ancestors.add(src)
                if not MorrisConsistencyCheck._prop_bwk(stn, u, terminated, ancestors = new_call_ancestors):
                    return False
            for v, delta in stn.predecessor_edges[u].items():
                if delta < 0:
                    continue
                new = dist[u] + delta
                if new < dist[v]:
                    dist[v] = new
                    heapq.heappush(queue, (new, v))
        terminated.add(src)
        return True

    @staticmethod
    def _is_negative_node(stn, node):
        for delta in stn.predecessor_edges[node].values():
            if delta < 0:
                return True
        return False
