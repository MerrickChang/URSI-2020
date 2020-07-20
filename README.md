## URSI 2020
My Work on my 2020 URSI

#Project Layout

* papers- contains reference materials for various algorithms

* proofs- any proofs I've done myself

    * random_consistent_stn_generation.pdf - my proofs for my custom random consistent STN generator

* src- source code repository

    * algorithms- various algorithms for stns

        * cordality (sic, I'll change it to the proper spelling later)- methods relating to chordality

            * triangulation.py (Triangulation)- various algorithms for converting an STN to triangular form

        * incremental- various incremental methods

            * matrix_update.py (MatrixUpdate)- various algorithms for incrementally updating an STN's distance matrix

            * solution_update.py (SolutionUpdate)- various algorithms for updating an STN's solutions

        * path_consist- methods relating to directed and partial path consistency

            * dpc.py (DirectedPathConsistency)- methods for converting an stn to a directed path consistent stn

            * ppc.py (PartialPathConsistency)- methods for converting an stn to a partially path consistent stn

            * dpc_dispatch.py (DPCDispatch)- dpc dispatcher mentioned in Planken (2013)

        * shortest_path- methods that calculate the distance matrix

            * bellman_ford.py (Bellman-Ford)- various implementations of Bellman-Ford

            * chelq.py (Chleq)- Chleq (1995) algorithm for the distance matrix

            * dijkstra.py (Dijkstra)- various implementations of Dijkstra's algorithm

            * floyd_warshall.py (FloydWarshall)- various implementations of Floyd-Warshall

            * johnson.py (Johnson)- various implementations of Johnson's algorithm

            * snowball.py (Snowball)- Planken (2013) algorithm for calculating the distance matrix

        * dispatch.py (Dispatch)- methods for converting networks to dispatchable form

        * dispatchability.py (Dispatchability)- contains greedy executer
	
	    * potential.py (Potential)- Hunsberger and Posenato algorithm for the potential function

        * tarjan.py (Tarjan)- (outdated, not functional) Sudais's implementation of Tarjan's algorithm

    * networks- code for STNs and STNUs and random generation

        * file_reader.py (FileReader)- reads STNs and STNUs

        * stn.py (STN)- STN class

        * stnu.py (STNU)- STNU class

        * random_stn.py (RandomSTN)- methods for random STN generation

    * test- various diagnostic tests I've designed

        * asap_test (ASAPTEST)- tests distance matrix calcualting methods

        * consistency_test (ConsistencyTest)- tests consistency checking methods

        * dpc_dispatch_test (DPCDispatchTest)- tests DPC dispatch on various PPC and DPC converters

        * progagating_test (PropagatingTest)- test incremental propagating algorithms

    * utils- code not directly related to STNs

        * probability (Probability)- various discrete distributions, specifically the binomial distribution; I use it for my random generation


Use the help() method for more detailed information on the contents of each class.

#Using the Test Functions

To use the test functions

1. Create a new instance with specified parameters. More details on what each parameter does can be accessed for each test using the help() function.

2. Add Simple Temporal Networks to the test queue for testing

3. Use the test's run function to activate the tests

For example,

    from src.tests.propagating_test import PropagatingTest

    test = PropagatingTest(verbose = True, logfile = "example4.txt", read_to_console=True)
    test.add_random_consistent_stns(10,6,8,0.7,-10,10)
    test.run()

will generate tests of propagating methods on 10 consistent stns with 6 to 8 vertices each saved under "example4.txt". 