class Dispatchability:
    def __init__(self):
        pass


    @staticmethod
    def _get_precessor_edges(stn, node_index):
        for edge_list in stn.successor_edges[:node_index]:
            for v, delta in edge_list:
                if v == node_index:
                    yield (v,delta)
        for edge_list in stn.successor_edges[node_index+1:]:
            for v, delta in edge_list:
                if v == node_index:
                    yield (v,delta)



    @staticmethod
    def _find_point_in_time_window(A, bounds):
        for i, time_point in enumerate(A):
            lower_bound, upper_bound = bounds[time_point]
            if lower_bound <= time and time <= upper_bound:
                yield A.pop(i)


    
    @staticmethod
    def greedy_execute(stn, start):
        p_inf = float("inf")
        n_inf = float("-inf")
        start_index = start
        time = 0
        length = len(stn.name_dict)
        n = range(length)
        if type(start) == str:
            start_index = stn.name_dict[start]
        A = [start_index]
        A_min = 0
        A_max = 0
        S = []
        bounds = []
        execution_time = []
        for x in n:
            bounds.append((n_inf, p_inf))
            execution_time.append(p_inf)
        bounds[start_index] = (0,0)
        while S < length:
            for time_point in Dispatchability._find_point_in_time_window(A, bounds):
                S.append(time_point)
                execution_time[time_point] = time
                for v,delta in stn.successor_edges[time_point]:
                    alt = time+delta
                    if alt <= bounds[1]:
                        bounds[1] = alt
                for _,v,delta in Dispatchability._get_precessor_edges(stn, time_point):
                    alt = delta-time
                    if bounds[v][0] <= alt:
                        bounds[v][0] = alt
                    if delta<0 and (not (v in A or v in S)):
                        A.append(v)
            A_min = min([bounds[l][0] for l in A])
            A_max = max([bounds[u][1] for u in A])
            if t<A_min:
                t = A_min
            assert t<A_max
        for point in S:
            print(point," at time ", execution_time[t],end=",")
