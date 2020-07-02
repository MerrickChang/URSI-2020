from src.tests.incremental_test import IncrementalTest
from src.tests.dispatch_test import DispatchabilityTest
from src.tests.johnson_test import JohnsonTest
from src.algorithms.dispatchability import Dispatchability
from src.networks.file_reader import FileReader
from src.tests.floyd_warshall_test import FloydWarshallTest
from src.tests.solution_update_test import SolutionUpdateTest
from src.tests.hp_test import HPTest
from src.networks.random_stn import RandomSTN
from src.algorithms.shortest_path.floyd_warshall import FloydWarshall
from src.tests.dispatcher_test import DispatcherTest

DispatcherTest(["fast_dispatch_APSP.stn", "slow_dispatch_APSP.stn"])
#johnson_test = JohnsonTest(["sample.stn", "sample2.stn", "sample3.stn"])
#floyd_warshall_test = FloydWarshallTest(["sample.stn", "sample2.stn", "sample3.stn"])
#ddispatch_test = DispatchabilityTest(["sample3.stn"])
#test = HPTest(10)
SolutionUpdateTest(10)
# for network in [RandomSTN.merrick_consistent_stn(5, 10, 0.7, -10, 10) for x in range(5)]:
#     print(network)
#     print(FloydWarshall.merrick_floyd_warshall(network))
##
# reader = FileReader()
# stn = reader.read_file("sample_dispatchable.stn")
# Dispatchability.greedy_execute(stn, "Z")
# Dispatchability.greedy_execute(stn, "B")
# Dispatchability.greedy_execute(stn, "C")
# Dispatchability.greedy_execute(stn, "E")
