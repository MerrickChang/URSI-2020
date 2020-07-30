##===================================
##File: test.py
##Author: Merrick Chang
##Date: July 2019
##===================================

from ..networks.file_reader import FileReader
from ..networks.random_stn import RandomSTN
import time
from datetime import datetime

class Test:
    """
    Parent class for all Tests
    """

    def __init__(self, verbose = False, logfile = False, read_to_console = True):
        self.networks = []
        self.network_source = []
        self.log = ""
        self.logfile = logfile
        self.verbose = verbose
        self.read_to_console = read_to_console
        self._set_test_methods()


    def _set_test_methods(self):
        pass



    def _pretest_network_changes(self, network):
        pass




    def addRandomConsistentSTNs(self, number_of_networks, min_no_of_nodes, max_no_of_nodes, edge_prob, min_weight, max_weight):
        generator = RandomSTN()
        for x in range(number_of_networks):
            self.networks.append(generator.merrick_consistent_stn(min_no_of_nodes, max_no_of_nodes, edge_prob, min_weight, max_weight))
            self.network_source.append("(STN generated using the merrick_consistent_stn function)")



    def addRandomSTNs(self, no_of_stns, max_no_of_nodes, max_weight=100, min_weight=-100):
        """

        """
        self.networks.extend(RandomSTN().random_stns(no_of_stns, max_no_of_nodes, max_weight=100, min_weight=-100))
        for x in range(no_of_stns):
            self.network_source.append("(STN generated using the random_stns function)")


    def addSTNFromFiles(self, filenames):
        """
        Adds networks from specified file names to be tested

        Input:
            filenames, list of files to be loaded for the test
        """
        reader = FileReader()
        for filename in filenames:
            self.networks.append(reader.read_file(filename))
            self.network_source.append("(STN loaded from "+ filename + ")")




    def _get_log_text_subentry(self, name, output, execution_time):
        return "\n\n" + name + " completed execution in " + str(execution_time) + "s.\nResulting Output:\n" + str(output) + "\n"




    def _get_entry_final_check(self, outputs):
        return ""




    def run(self):
        """
        Tests all the methods on the desired networks

        Effects:
            If read_to_console is True, outputs results to command line
            If logging file is specified, logs results to specified location
                (If verbose, logs contain more detail on the STN)
        """
        i = 1
        self.log += "Test of " + self.test_name + "\n Merrick Chang \n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"
        if self.read_to_console:
            print(self.log)
        for network in self.networks:
            self._pretest_network_changes(network)
            entry = "============================================\nTEST " + str(i) + ":\n"
            if self.verbose:
                entry += str(network)
            else:
                entry += "Number of nodes: " + network.length + ", Number of edges: " + sum([len(edges) for edges in network.successor_edges])+"\n"
            entry += self.network_source[i-1] + "\n"
            outputs = []
            for name, method in self.test_methods.items():
                start = time.time()
                output = method(network)
                outputs.append(output)
                stop = time.time()
                execution_time = stop - start
                entry += self._get_log_text_subentry(name, output, execution_time)
            entry += self._get_entry_final_check(outputs) + "============================================\n"
            self.log += entry
            if self.read_to_console:
                print(entry)
            i+=1
        if self.logfile:
            with open(self.logfile, "w") as file:
                file.write(self.log)
