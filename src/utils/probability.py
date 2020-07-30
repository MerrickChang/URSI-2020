##===================================
##File: probability.py
##Author: Merrick Chang
##Date: July 2019
##===================================
from random import random
import math

class Probability:
    @staticmethod
    def binom_dist(num_events, prob):
        roll = random()
        for x, cum_mass in enumerate(Probability._binomial_cmf(num_events, prob)):
            if roll < cum_mass:
                return x
        return num_events

    @staticmethod
    def _binomial_cmf(num_events, prob):
        mass = math.pow((1-prob), num_events)
        cmf = 0
        for k in range(0, num_events+1):
            cmf += mass
            yield cmf
            mass = mass * prob / (1-prob) * (num_events - k)/(k+1)
