class Dispatchability:
    def __init__(self):
        pass


    @staticmethod
    def _get_precessor_edges(stn, node_index):
        for u, edge_list in enumerate(stn.successor_edges[:node_index]):
            for v, delta in edge_list.items():
                if v == node_index:
                    yield (u, delta)
        for u, edge_list in enumerate(stn.successor_edges[node_index+1:], start=node_index+1):
            for v, delta in edge_list.items():
                if v == node_index:
                    yield (u, delta)



    @staticmethod
    def _find_point_in_time_window(A, bounds, time):
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
        length = len(stn.names_dict)
        n = range(length)
        if type(start) == str:
            start_index = stn.names_dict[start]
        A = [start_index]
        A_min = 0
        A_max = 0
        S = []
        bounds = []
        execution_time = []
        for x in n:
            bounds.append([n_inf, p_inf])
            execution_time.append(p_inf)
        bounds[start_index] = [0,0]
        print(stn.names_dict)
        while len(S) < length:
            assert len(A) != 0, "There are no more enabled points. This STN is not dispatchable."
            A_min = min([bounds[l][0] for l in A])
            A_max = min([bounds[u][1] for u in A])
            if time<A_min:
                time = A_min
            print("Time =", time)
            assert time<=A_max, "The time exceeds the maximum value in the enabled points. This STN is not dispatchable."
            for time_point in Dispatchability._find_point_in_time_window(A, bounds, time):
                if not time_point in S:
                    S.append(time_point)
                execution_time[time_point] = time
                for v,delta in stn.successor_edges[time_point].items():
                    alt = time+delta
                    if bounds[v][1] >= alt:
                        bounds[v][1] = alt
                for u,delta in Dispatchability._get_precessor_edges(stn, time_point):
                    alt = time-delta
                    if alt >= bounds[u][0]:
                        bounds[u][0] = alt
            for u, edge_dict in enumerate(stn.successor_edges):
                if not (u in A or u in S):
                    neg_edges_lead_to_S = True
                    for v, delta in stn.successor_edges[u].items():
                        if delta<0 and v not in S:
                            neg_edges_lead_to_S = False
                            break
                    if neg_edges_lead_to_S: 
                        A.append(u)
        for point in S:
            print(stn.names_list[point]," at time ", execution_time[point],end=",")
