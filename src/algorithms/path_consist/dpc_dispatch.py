import random


class DPCDispatch:

    @staticmethod
    def dpc_dispatch(stn, seq, min_window = -100, max_window = 100):
        time_windows = []
        neighboor_hoods = []
        schedule = []
        if not stn.predecessor_edges:
            stn.update_predecessors()
        for n in range(stn.length):
            time_windows.append([min_window, max_window])
            schedule.append(float("inf"))
            neighbors = set(stn.successor_edges[n].keys())
            neighbors.update(stn.predecessor_edges[n].keys())
            neighboor_hoods.append(neighbors)
        for k, v in enumerate(seq):
            min_time, max_time = time_windows[v]
            schedule[v] = random.randint(min_time, max_time)
            for neighbor in neighboor_hoods[v]:
                alt_min = float("-inf")
                alt_max = float("inf")
                if neighbor in stn.predecessor_edges[v]:
                    alt_min = stn.predecessor_edges[v][neighbor] - schedule[v]
                    if time_windows[neighbor][0] < alt_min:
                        time_windows[neighbor][0] = alt_min
                if neighbor in stn.successor_edges[v]:
                    alt_max = stn.successor_edges[v][neighbor] + schedule[v]
                    if time_windows[neighbor][0] > alt_max:
                        time_windows[neighbor][0] = alt_max
        return schedule
