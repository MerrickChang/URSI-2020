import random


class DPCDispatch:
    """
    Static methods related to the DPC-Dispatch algorithm from Planken (2013)
    """

    @staticmethod
    def dpc_dispatch(stn, seq, min_window = -1000, max_window = 1000):
        """
        DPC-Dispatch algorithm from Planken (2013)
        -------------------------------------------------------------------
        Input:
            stn, the target STN
            seq, an ordering for the vertices in the STN in the form of a list of ints
            min_window, a minimum time within which all the time points are executed
            max_window, a maximum time within which all the time points are executed

        Output:
            schedule, an list of ints representing the execution times
        -------------------------------------------------------------------
        """
        time_windows = []
        neighboor_hoods = []
        schedule = []
        if not stn.predecessor_edges or not stn.pred_edges_up_to_date:
            stn.update_predecessors()
        for n in range(stn.length):
            time_windows.append([min_window, max_window])
            schedule.append(float("inf"))
            neighbors = set(stn.successor_edges[n].keys())
            neighbors.update(stn.predecessor_edges[n].keys())
            neighboor_hoods.append(neighbors)
        for k, v in enumerate(seq):
            min_time, max_time = time_windows[v]
            try:
                schedule[v] = random.randint(min_time, max_time)
            except ValueError:
                print("Error: Min-Time Exceeds Max-Time... The Max-Window Is Likely Too Low")
                return False
            for neighbor in neighboor_hoods[v]:
                if seq.index(neighbor) > k:
                    if neighbor in stn.predecessor_edges[v]:
                        alt_min = schedule[v] - stn.predecessor_edges[v][neighbor]
                        if time_windows[neighbor][0] < alt_min:
                            time_windows[neighbor][0] = alt_min
                    if neighbor in stn.successor_edges[v]:
                        alt_max = stn.successor_edges[v][neighbor] + schedule[v]
                        if time_windows[neighbor][1] > alt_max:
                            time_windows[neighbor][1] = alt_max
        return schedule
