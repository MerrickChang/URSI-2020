from src.tests.incremental_test import IncrementalTest
from src.tests.dispatch_test import DispatchabilityTest
from src.algorithms.dispatchability import Dispatchability
from src.networks.file_reader import FileReader

for x in range(40):
    print("Test ", x, ":")
    test = IncrementalTest(["sample_dispatchable.stn"])
    
##
##reader = FileReader()
##stn = reader.read_file("sample_dispatchable.stn")
##Dispatchability.greedy_execute(stn, "Z")
