from ..algorithms.incremental.solution_update import SolutionUpdate
from .test import Test
from ..algorithms.dispatchability import Dispatchability
import random

class SolutionUpdateTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            u, v = random.sample(range(len(network.names_list)), 2)
            while v in network.successor_edges[u]:
                u, v = random.sample(range(len(network.names_list)), 2)
            delta = random.choice(list(range(-10,11)))
            print(u,v,delta)
            solution = Dispatchability.greedy_execute(network, network.names_list[0])
            print(solution)
            s_prime  = SolutionUpdate.rsjm(network, solution, (u,v,delta))
            print(s_prime)
            if s_prime:
                print(Dispatchability._check_solution(network, s_prime))
            else:
                print("Adding constraint makes system infeasible.")
