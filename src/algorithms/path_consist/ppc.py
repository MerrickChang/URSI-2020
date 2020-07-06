class PartialPathConsistency:
    @staticmethod
    def convert_to_PPC(stn): #WIP
        """
        Takes a cordal STN and outputs a partially path consistent STN
        """
        stn.pred_edges_up_to_date = False
        queue = []
        for u, edge_list in enumerate(stn.successor_edges):
            for v, delta in edge_list:
                if u >= v:
                    break
                queue.append((u,v))
        while len(queue) != 0:
            u,v = queue.pop()
            for x in range(stn.length):
                if x==u or x==v:
                    continue
                pass
