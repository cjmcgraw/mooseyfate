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

    def fitness(self):
        return 1.0

    def get_guess(self, vector):
        if random() <= self.p_value():
            return True
        return False

    def update(self, vector, attacked, outcome):
        if attacked:
            if outcome == 1:
                self._training_hits += 1
            self._training_n += 1

    def p_value(self):
        if self._training_n < 50:
            return 1.0
        return self._training_hits / self._training_n

if __name__ == "__main__":

    from TestingEnvironment import monster_generator, run_tests

    # Initial training period
    hypothesis = AdaptiveDistributionHypothesis()
    monsters = monster_generator()

    for x in range(100):
        monster = next(monsters)
        outcome = monster.action(True)
        hypothesis.update(monster, True, outcome)

    run_tests(hypothesis, 5000)

    print(vars(hypothesis))
    print(hypothesis.p_value())
