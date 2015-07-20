"""This hypothesis represents the simple probability
distrubition. It assumes that there is a standard distribution
for the data. It attempts to determine that distribution without
reference to classification or conditional probabilities
"""
from random import random

from Hypothesis import Hypothesis

class SimpleProbabilityHypothesis(Hypothesis):

    def __init__(self):
        self._training_n = 0
        self._training_hits = 0.0
        self.name = "SimpleProbabilityHypothesis"

    def getName(self):
        return self.name;

    def fitness(self):
        # Fitness returns 1.0 for sanity check
        # If algorithm ever produces anything
        # useful then we will use a rolling window
        # and a comparison of the squared
        # expected values to make sense of the fitness
        return 1.0

    def get_guess(self, vector):
        if random() <= self.p_value():
            return True
        return False

    def update(self, vector, attacked, outcome):
        # Currently using naive case of automatic
        # updating every iteration. This is for a
        # sanity check. 
        # 
        # If sanity check passes then we can update
        # based off of distance of expected values
        # using the standard measurement for the
        # poisson distribution
        if attacked:
            if outcome == 1:
                self._training_hits += 1
            self._training_n += 1

    def p_value(self):
        if self._training_n < 50:
            return 1.0
        return self._training_hits / self._training_n

if __name__ == "__main__":

    from ..lib.TestingEnvironment import monster_generator, run_tests, aggro_probability, passive_probability

    # Initial training period
    hypothesis = SimpleProbabilityHypothesis()
    monsters = monster_generator()

    for x in range(100):
        monster = next(monsters)
        outcome = monster.action(True)
        hypothesis.update(monster, True, outcome)

    run_tests(hypothesis, 5000)

    print("Hypothesis p-value :" + str(hypothesis.p_value()))
