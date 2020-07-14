# URSI 2020
 My Work on my 2020 URSI

Folders:

* papers- contains reference materials for various algorithms

* proofs- any proofs I've done myself

    * random_consistent_stn_generation.pdf - my proofs for my custom random consistent STN generator

* src- source code repository

    * algorithms- various algorithms for stns

        * cordality (sic, I'll change it to the proper spelling later)- methods relating to chordality

            * triangulation.py- various algorithms for converting an STN to triangular form

        * incremental- various incremental methods

            * matrix_update.py- various algorithms for incrementally updating an STN's distance matrix

            * solution_update.py- various algorithms for updating an STN's solutions

        * path_consist- methods relating to directed and partial path consistency

            * dpc.py- methods for converting an stn to a directed path consistent stn

            * ppc.py- methods for converting an stn to a partially path consistent stn

            * dpc_dispatch.py- dpc dispatcher mentioned in Planken (2013)

        * shortest_path- methods that calculate the distance matrix

            * bellman_ford.py - various implementations of Bellman-Ford

            * chelq.py- Chleq (1995) algorithm for the distance matrix

            * dijkstra.py- various implementations of Dijkstra's algorithm

            * floyd_warshall.py- various implementations of Floyd-Warshall

            * johnson.py- various implementations of Johnson's algorithm

            * snowball.py- Planken (2013) algorithm for calculating the distance matrix

        * dispatch.py- methods for converting networks to dispatchable form

        * dispatchability.py- primarily, contains greedy executer
	
	* potential.py- Hunsberger and Posenato algorithm for the potential function

        * tarjan.py- (outdated, not functional) Sudais's implementation of Tarjan's algorithm

    * networks- code for STNs and STNUs and random generation

        * file_reader.py- reads STNs and STNUs

        * stn.py- STN class

        * stnu.py- STNU class

        * random_stn.py- methods for random STN generation

    * test- various diagnostic tests I've designed for my purposes

    * utils- code not directly related to STNs

        * probability- various discrete distributions, specifically the binomial distribution; I use it for my random generation 