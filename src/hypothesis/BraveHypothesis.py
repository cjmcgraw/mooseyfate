"""Brave Hypothesis represents the standard hypothesis
to always attack, irregardless of the aggressiveness
of the monster"""

from Hypothesis import Hypothesis

class BraveHypothesis(Hypothesis):

    def __init__(self):
        self.name = "Brave"
        self._n = 0
        self._hits = 0.0

    def fitness(self):
        """Brave hypothesis is the default hypothesis for the first
        100 tests. This is because the only way to really determine
        if a monster is aggressive/passive is to attack them. Therefore
        the information gathering phase requires attacking with bravery
        """
        if self._n < 100:
            return 1.0
        return self._hits / self._n

    def get_guess(self, vector):
        """The Brave hypothesis always attacks"""
        return True

    def update(self, vector, attacked, outcome):
        """The Brave hypothesis keeps a average on how its doing.
        This is used to calculate the fitness beyond the initial
        100 tests"""
        if attacked and outcome == 1:
            self._hits += 1
        self._n += 1

    def getName(self):
        return self.name;
