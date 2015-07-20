"""
    Simple Wimpy Hypothesis: ... because who would wants to be killed by monsters, no one.

        Fitness is determined via a ratio of how right a coward's pattern is given observed attacks

        Idea: Wimpy hypothesis may converge to peak fitness if a large number of attacks are observed

"""


from Hypothesis import Hypothesis

class WimpyHypothesis(Hypothesis):

    def __init__(self):
        self._n = 0
        self._amountWeWereAttacked = 0
        self._amountWeRanAway = 0
        self.name = "WimpyHypothesis"

    def getName(self):
        return self.name;

    def fitness(self):
        if self._amountWeRanAway == 0:
            return 0;
        wimpyFitness = self._amountWeWereAttacked / self._amountWeRanAway
        return wimpyFitness

    def get_guess(self, vector):
        """Wimpy never attacks"""
        """We outnumber them! Charge! Charge! Hey, where'd you guys go? Retreat! Retreat!" --Withdraw MTG"""
        return False

    def update(self, vector, attacked, outcome):
          """If we're attacked record it. Know that we would've run away, yo."""
        if attacked:
            self._amountWeWereAttacked = self._amountWeWereAttacked + 1

        """We always run away """
        self._amountWeRanAway = self._amountWeRanAway + 1
        self._n += 1
        return 0

        return 0
