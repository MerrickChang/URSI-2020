from .test import Test
from ..algorithms.shortest_path.chleq import Chleq
from ..algorithms.shortest_path.snowball import Snowball
from ..algorithms.shortest_path.floyd_warshall import FloydWarshall
from ..algorithms.shortest_path.johnson import Johnson
import copy

class ASAPTest(Test):
    """
    A test for the algorithms which calculate the distance matrix.
    """

    def __init__(self, verbose = True, logfile = False, read_to_console = False):
        """

        """
        self.test_name = "ASAP Methods"
        super().__init__(verbose, logfile, read_to_console)



    def _set_test_methods(self):
        self.test_methods = {
            "CHLEQ": lambda stn : Chleq.get_distance_matrix(copy.deepcopy(stn), list(range(stn.length))),
            "FLOYD-WARSHALL": lambda stn : FloydWarshall.merrick_floyd_warshall(stn),
            "JOHNSON": lambda stn : Johnson.merrick_johnson(stn),
            "SNOWBALL": lambda stn : Snowball.snowball(copy.deepcopy(stn), list(range(stn.length)))
            }



    def _get_entry_final_check(self, outputs):
        for x in range(len(outputs)-1):
            if outputs[x] != outputs[x+1]:
                return "\nFailure, outputs are not all equal\n"
        return "\nSuccess, outputs are equal\n"



    def _get_log_text_subentry(self, name, output, execution_time):
        if self.verbose:
            return "\n\n" + name + " completed execution in " + str(execution_time) + ".\nOutput:\n[" + ",\n".join([str(x) for x in output]) + "]"
        else:
            return "\n\n" + name + " completed execution in " + str(execution_time) + "."
