"""Simple Wimpy Hypothesis: ... because who would wants to be killed by monsters, no one.
Fitness is determined via a ratio of how right a coward's pattern is given observed attacks
Idea: Wimpy hypothesis may converge to peak fitness if a large number of attacks are observed
"""
from Hypothesis import Hypothesis

class WimpyHypothesis(Hypothesis):

    def __init__(self):
        self._losses = 0.0
        self._n = 0.0
        self._limiting = 100

    def name(self):
        return "WimpyHypothesis"

    def fitness(self):
        if not self._n:
            return 0;
        return (self._losses / self._n)

    def get_guess(self, vector):
        """Wimpy never attacks"""
        """We outnumber them! Charge! Charge! Hey, where'd you guys go? Retreat! Retreat!" --Withdraw MTG"""
        return False

    def update(self, vector, attacked, outcome):
        """If we're attacked record it. Know that we would've run away, yo."""

        #Note: Capped of at self._limiting iterations

        if self._limiting >  0:
            if attacked == 1:
                if outcome == -1:
                    self._losses += 1
                self._n += 1

        self._limiting -= 1
