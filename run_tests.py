from src.tests.incremental_test import IncrementalTest

for x in range(100):
    print("Test ", x, ":")
    test = IncrementalTest(["sample_dispatchable.stn"])
    
