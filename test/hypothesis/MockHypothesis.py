"""Simple mock hypothesis ensuring that the decisioner
is operating correctly
"""
from src.hypothesis.Hypothesis import Hypothesis

class MockHypothesis(Hypothesis):

    def __init__(self, next_guess=False, fitness=0.0):
        self._next_guess = next_guess
        self._fitness = fitness
        self._times_updated = 0

    def fitness(self):
        return self._fitness

    def get_guess(self, vector):
        return self._next_guess

    def update(self, vector, attacked, outcome):
        self._times_updated += 1
