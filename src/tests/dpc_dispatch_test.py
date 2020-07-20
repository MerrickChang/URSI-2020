from .test import Test
from ..algorithms.path_consist.dpc_dispatch import DPCDispatch
from ..algorithms.path_consist.dpc import DirectedPathConsistency as DPC
from ..algorithms.path_consist.ppc import PartialPathConsistency as PPC
import random
import copy

class DPCDispatchTest(Test):
    """
    A test for the algorithms which calculate the distance matrix.
    """

    def __init__(self, verbose = True, logfile = False, read_to_console = False, min_window = -1000, max_window = 1000):
        """

        """
        self.test_name = "DPC-Dispatch On Different Conversion Methods"
        self.min_window = min_window
        self.max_window = max_window
        super().__init__(verbose, logfile, read_to_console)



    def _set_test_methods(self):
        self.test_methods = {
            "DIRECTED PATH CONSISTENCY (PLANKEN) [1]": self._check_dpc,
            "DIRECTED PATH CONSISTENCY (PLANKEN) [2]": self._check_dpc,
            "DIRECTED PATH CONSISTENCY (PLANKEN) [3]": self._check_dpc,
            "P3C (PLANKEN) [1]": self._check_p3c,
            "P3C (PLANKEN) [2]": self._check_p3c,
            "P3C (PLANKEN) [3]": self._check_p3c
            }




    def _get_random_vertex_ordering(self, stn):
        ordering = list(range(stn.length))
        random.shuffle(ordering)
        return ordering



    def _check_dpc(self, stn):
        seq = self._get_random_vertex_ordering(stn)
        modified = DPC.convert_to_DPC(copy.deepcopy(stn), seq)
        if stn:
            solution = DPCDispatch.dpc_dispatch(modified, seq, min_window=self.min_window, max_window=self.max_window)
            if solution:
                return solution, stn.check_solution(solution)
            else:
                return False
        else:
            return "The network is inconsistent."


    def _check_p3c(self, stn):
        seq = self._get_random_vertex_ordering(stn)
        modified = PPC.P3C(copy.deepcopy(stn), seq)
        if stn:
            solution = DPCDispatch.dpc_dispatch(modified, seq, min_window=self.min_window, max_window=self.max_window)
            if solution:
                return solution, stn.check_solution(solution)
            else:
                return False
        else:
            return "The network is inconsistent."


    def _get_log_text_subentry(self, name, output, execution_time):
        subentry = "\n\n" + name + " completed execution in " + str(execution_time)
        if type(output) == str:
            subentry += "\n" + output
        elif self.verbose:
            if output:
                subentry += "\nOutput:\n" + str(output[0]) + "\n"
            else:
                subentry+= "Error: Dispatcher fails"

        return subentry
