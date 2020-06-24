from src.tests.incremental_test import IncrementalTest
from src.tests.dispatch_test import DispatchabilityTest
from src.tests.johnson_test import JohnsonTest
from src.algorithms.dispatchability import Dispatchability
from src.networks.file_reader import FileReader
from src.tests.floyd_warshall_test import FloydWarshallTest
from src.tests.solution_update_test import SolutionUpdateTest

#johnson_test = JohnsonTest(["sample.stn", "sample2.stn", "sample3.stn"])
#floyd_warshall_test = FloydWarshallTest(["sample.stn", "sample2.stn", "sample3.stn"])
#ddispatch_test = DispatchabilityTest(["sample3.stn"])
test = SolutionUpdateTest(20)

##
# reader = FileReader()
# stn = reader.read_file("sample_dispatchable.stn")
# Dispatchability.greedy_execute(stn, "Z")
# Dispatchability.greedy_execute(stn, "B")
# Dispatchability.greedy_execute(stn, "C")
# Dispatchability.greedy_execute(stn, "E")
