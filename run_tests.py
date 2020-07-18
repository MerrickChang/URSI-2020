from src.tests.asap_test import ASAPTest

test = ASAPTest(verbose = True, logfile = "example.txt", read_to_console=True)
test.addRandomConsistentSTNs(10,6,8,0.7,-10,10)
test.run()
