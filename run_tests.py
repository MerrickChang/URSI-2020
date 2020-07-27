from src.tests.consistency_test import ConsistencyTest

test = ConsistencyTest(verbose = True, logfile = "verify.txt", read_to_console=True)
test.addRandomConsistentSTNs(10, min_no_of_nodes = 6, max_no_of_nodes = 8, edge_prob = 0.7, min_weight = -10, max_weight = 10)
test.run()
