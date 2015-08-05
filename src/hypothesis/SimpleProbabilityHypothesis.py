"""This hypothesis represents the simple probability
distrubition. It assumes that there is a standard distribution
for the data. It attempts to determine that distribution without
reference to classification or conditional probabilities
"""
from random import random

from Hypothesis import Hypothesis

class SimpleProbabilityHypothesis(Hypothesis):

    def __init__(self):
        super(SimpleProbabilityHypothesis, self).__init__()
        self._training_n = 0
        self._training_hits = 0.0

    def name(self):
        return "SimpleProbabilityHypothesis (p = " + str(self.p_value()) + ")"

    def get_guess(self, vector):
        if random() <= self.p_value():
            return True
        return False

    def update(self, vector, attacked, outcome):
        # Currently using naive case of automatic
        # updating every iteration.
        # 
        # Ideally we would be able to utilize a
        # sliding window that contains its own
        # expected value that can be measured
        # vs the poisson distribution test for
        # the current probabilty.
        #
        # If our probability falls outside of
        # acceptance then we could replace the
        # current p with the sliding window p.
        #
        # However for now that is beyond the scope
        # of this initial implementation
        super(SimpleProbabilityHypothesis, self).update(vector, attacked, outcome)
        if attacked:
            if outcome == 1:
                self._training_hits += 1
            self._training_n += 1

    def p_value(self):
        if self._training_n < 50:
            return 1.0
        return self._training_hits / self._training_n
