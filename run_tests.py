from src.tests.asap_test import ASAPTest

test = ConsistencyTest(verbose = True, logfile = "verify.txt", read_to_console=True)
test.add_random_consistent_stns(10,6,8,0.7,-10,10)
test.run()
