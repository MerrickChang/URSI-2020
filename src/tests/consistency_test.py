from .test import Test
from ..algorithms.shortest_path.floyd_warshall import FloydWarshall
from ..algorithms.shortest_path.bellman_ford import BellmanFord
from ..algorithms.path_consist.dpc import DirectedPathConsistency as DPC
from ..algorithms.path_consist.ppc import PartialPathConsistency as PPC
from ..algorithms.morris import MorrisConsistencyCheck
import random
import copy

class ConsistencyTest(Test):
    """
    A test for the algorithms which calculate the distance matrix.
    """

    def __init__(self, verbose = True, logfile = False, read_to_console = False):
        """

        """
        self.test_name = "Consistency Methods"
        super().__init__(verbose, logfile, read_to_console)



    def _set_test_methods(self):
        self.test_methods = {
            #"BANNISTER-EPPSTEIN": lambda stn : True if BellmanFord.bannister_eppstein(stn) else False,
            "BELLMAN-FORD": lambda stn : True if BellmanFord.merrick_bellman_ford(stn) else False,
            "DIRECTED PATH CONSISTENCY (PLANKEN)": lambda stn : True if DPC.convert_to_DPC(copy.deepcopy(stn), ConsistencyTest._get_random_vertex_ordering(stn)) else False,
            "FLOYD-WARSHALL": lambda stn : True if FloydWarshall.merrick_floyd_warshall(stn) else False,
            "MORRIS": MorrisConsistencyCheck.is_consistent,
            "P3C (PLANKEN)": lambda stn : True if PPC.P3C(copy.deepcopy(stn), ConsistencyTest._get_random_vertex_ordering(stn)) else False
            }




    @staticmethod
    def _get_random_vertex_ordering(stn):
        ordering = list(range(stn.length))
        random.shuffle(ordering)
        return ordering


    def _get_entry_final_check(self, outputs):
        for x in range(len(outputs)-1):
            if outputs[x] != outputs[x+1]:
                return "\nFailure, outputs are not all equal\n"
        return "\nSuccess, outputs are equal\n"
