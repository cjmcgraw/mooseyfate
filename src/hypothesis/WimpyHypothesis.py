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

    def fitness(self):
        wimpyFitness = self._amountWeWereAttacked / self._amountWeRanAway
        return wimpyFitness

    def get_guess(self, vector):
        """Wimpy never attacks"""
        """We outnumber them! Charge! Charge! Hey, where'd you guys go? Retreat! Retreat!" --Withdraw MTG"""
        return False

    def update(self, vector, attacked, outcome):
        """If we're attacked record it. Know that we would've run away, yo."""
        if attacked:
            self.__amountAttacked__ = self.__amountAttacked__ + 1

        """We always run away """
        self.__amountWeRanAway__ = self.__amountWeRanAway__ + 1

        return 0
