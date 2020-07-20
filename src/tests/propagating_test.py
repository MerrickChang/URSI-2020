import random
import copy
from .test import Test
from ..algorithms.incremental.matrix_update import DistanceMatrixUpdate as DMU
from ..algorithms.incremental.solution_update import SolutionUpdate as SU
from ..algorithms.shortest_path.johnson import Johnson
from ..algorithms.shortest_path.bellman_ford import BellmanFord

class PropagatingTest(Test):
    """
    A test for the algorithms which propogating updates.

    Warning: Test is only designed to work with consistent STNs. Non-consistent STNS may produce unpredictable results.
    """

    def __init__(self, verbose, logfile, read_to_console):
        """
        Default constructor for the PropogatingTest Class
        -------------------------------------------------------------------------------------------------
        Inputs:
            verbose, a boolean which determines how much detail the log readouts should contain
            logfile, False if the current test session should not be recorded; else a string representing the logfile name
            read_to_console, a boolean representing whether or not the test results should be written to the command line
        --------------------------------------------------------------------------------------------------
        """
        super().__init__(verbose, logfile, read_to_console)


    def _set_test_methods(self):
        self.test_name = "Propogating Methods"
        self.test_methods = {
            "Distance Matrix Update (Backwards-Propogating)": self._dm_test,
            "Potential Update (Ramalingam et al., Backwards-Propogating)": self._rsjm_bwk_test,
            "Potential Update (Ramalingam et al., Forwards-Propogating)": self._rsjm_fwd_test,
            "Potential Update (Hunsberger and Posenato, Backwards-Propogating)":self._hp_test
            }


    def _pretest_network_changes(self, stn):
        self.original_distance_matrix = Johnson.merrick_johnson(stn)
        self.removed_link = random.choice([(u,v,delta)
                                            for u, edge_list in enumerate(stn.successor_edges)
                                            for v, delta in edge_list.items()
                                            ])
        stn.successor_edges[self.removed_link[0]].pop(self.removed_link[1])
        stn.pred_edges_up_to_date = False
        self.new_distance_matrix = Johnson.merrick_johnson(stn)
        self.potential_function = BellmanFord.merrick_bellman_ford(stn)
        self.potential_function.pop()



    def _rsjm_fwd_test(self, stn):
        dup = copy.deepcopy(stn)
        result = SU.rsjm_fwd(dup, self.potential_function, self.removed_link)
        if dup.check_solution(result):
            return result
        else:
            return False



    def _rsjm_bwk_test(self, stn):
        dup = copy.deepcopy(stn)
        dup.pred_edges_up_to_date = False
        result = SU.rsjm_bwk(dup, self.potential_function, self.removed_link)
        if dup.check_solution(result):
            return result
        else:
            print(self.removed_link)
            print(self.potential_function)
            print(result)
            return False



    def _dm_test(self, stn):
        result = DMU.propagation(stn, self.new_distance_matrix, self.removed_link)
        if result == self.original_distance_matrix:
            return result
        else:
            print(self.removed_link)
            print(result)
            print(self.original_distance_matrix)
            return False



    def _hp_test(self, stn):
        dup = copy.deepcopy(stn)
        u,v,delta = self.removed_link
        dup.successor_edges[u][v] = delta
        result = SU.update_potential(dup, v, self.potential_function)
        if dup.check_solution(result):
            return result
        else:
            return False




    def _get_log_text_subentry(self, name, output, execution_time):
        if output:
            if self.verbose:
                return "\n\n" + name + " completed execution in " + str(execution_time) + "s.\nResulting Output:\n" + str(output) + "\n"
            else:
                return "\n\n" + name + " completed execution in " + str(execution_time) + ". Output is correct."
        else:
            return "\n\n" + name + " completed execution in " + str(execution_time) + ". Error: Incorrect output."
