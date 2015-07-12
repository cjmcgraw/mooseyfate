"""The WimpyHypothesis is the exact opposite of the
BraveHypothesis. It always avoids attacking."""

from Hypothesis import Hypothesis

class WimpyHypothesis(Hypothesis):

    def __init__(self):
        self._n = 0
        # TODO: Decide which variables to track for fitness

    def fitness(self):
        # TODO: Determine how to decide on fitnes

    def get_guess(self, vector):
        """Wimpy never attacks"""
        return False

    def update(self, vector, attacked, outcome):
        # TODO: Determine how to update fitness
