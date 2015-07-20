"""
    Simple Wimpy Hypothesis: ... because who would wants to be killed by monsters, no one.

        Fitness is determined via a ratio of how right a coward's pattern is given observed attacks
        
        Idea: Wimpy hypothesis may converge to peak fitness if a large number of attacks are observed
        
"""

from Hypothesis import Hypothesis


class ChunkyWimpyHypothesis(Hypothesis):
    def __init__(self):
        self._n = 0
        self._amountWeWereAttacked = 0
        self._amountWeRanAway = 0
        self.__arrayOfTimesWeWereAttacked = [0, 0, 0, 0, 0]
        self.__arrayOfTimesWeRanAway = [1, 1, 1, 1, 1]
        self.__chunkCardinality = len(self.__arrayOfTimesWeRanAway)
        self.__currentChunk = 0
        self.name = "ChunkyWimpy"

    def getName(self):
        return self.name;

    def fitness(self):
        if 0 == sum(self.__arrayOfTimesWeRanAway) :
            return 0
        chunkedWimpyFitness = sum(self.__arrayOfTimesWeWereAttacked) / sum(self.__arrayOfTimesWeRanAway)
        return chunkedWimpyFitness

    def get_guess(self, vector):
        """Wimpy never attacks"""
        """We outnumber them! Charge! Charge! Hey, where'd you guys go? Retreat! Retreat!" --Withdraw MTG"""
        return False

    def update(self, vector, attacked, outcome):
        """If we're attacked record it. Know that we would've run away, yo."""
        if attacked:
            self.__arrayOfTimesWeWereAttacked[self.__currentChunk] = 1
        else:
            self.__arrayOfTimesWeWereAttacked[self.__currentChunk] = 0

        """We always run away """
        self.__arrayOfTimesWeRanAway[self.__currentChunk] = 1

        """update current chunk mod its cardinality"""
        self.__currentChunk = self.__currentChunk % self.__chunkCardinality

        return 0
