from src.tests.consistency_test import ConsistencyTest

test = ConsistencyTest(verbose = True, logfile = "verify.txt", read_to_console=True)
test.addRandomSTNs(100, 8)
test.run()
