from ..algorithms.incremental.solution_update import SolutionUpdate
from .test import Test
from ..algorithms.dispatchability import Dispatchability
import random
from ..algorithms.dispatch import Dispatch
class SolutionUpdateTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for x, network in enumerate(self.networks):
            print("===================Test ", x, "============================")
            x = 0
            for x in range(100):
                u, v = random.sample(range(len(network.names_list)), 2)
            delta = random.choice(list(range(-10,11)))
            if x==100:
                print("Cannot find new edge, skipping test")
                continue
            try:
                network = Dispatch.convert_to_dispatchable(network)
                if network:
                    print(network)
                    solution = False
                    for x, edges in enumerate(network.successor_edges):
                        any_negative = False
                        for delta in edges.values():
                            if delta<0:
                                any_negative = True
                                break
                        if not any_negative:
                            print(x)
                            solution = Dispatchability.greedy_execute(network, x)
                            break
                    assert solution
                    print(u,v,delta)
                    print(solution)
                    s_prime  = SolutionUpdate.rsjm(network, solution, (u,v,delta))
                    s_prime2 = SolutionUpdate.update_potential(network, h=solution, A=v)
                    if s_prime:
                        print(s_prime)
                    else:
                        print("Adding constraint makes system infeasible.")
                    if s_prime2:
                        print(s_prime2)
                    else:
                        print("Adding constraint makes system infeasible.")
                else:
                    print("Infeasible, skipping test")
            except AssertionError as error:
                print(error)
