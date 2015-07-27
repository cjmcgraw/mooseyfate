""" Rando Hypothesis flips a coin and sets a fitness value
"""
import random
from Hypothesis import Hypothesis

class RandoHypothesis(Hypothesis):

    def __init__(self):
        self._wins = 0.0
        self._n = 0.0
        self._limiting = 100
        self._lastGuess = False

    def getName(self):
        return "RandoHypothesis"

    def fitness(self):
        if not self._n:
            return 0;
        return self._wins / self._n

    def get_guess(self, vector):
        """Get a random guess by calling heads"""
        flippedCoin = random.uniform(0.0, 1.0)
        heads = flippedCoin > 0.5
        if heads:
            self._lastGuess = True
            return True
        else:
            self._lastGuess = False
            return False

    def update(self, vector, attacked, outcome):
        if attacked == 1:
            if outcome == 1 and self._lastGuess:
                self._wins += 1
            self._n += 1

        """In case we're not the selected algorithm
           we must update the stored random guess
           this will update self._lastGuess"""
        local_guess = self.get_guess(vector)
