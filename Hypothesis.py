"""Hypothesis module defines the Hypothesis abstract class """

from abc import ABCMeta, abstractmethod

class Hypothesis:
    """Defines the Hypothesis required methods"""

    __metaclass__ = ABCMeta

    def __init__(self):
        """ Initialize with initialization bias """
        pass

    @abstractmethod
    def fitness(self):
        """Retrieves a float representing the fitness of
        this hypothesis to its previous data

        :return: float
        """
        pass

    @abstractmethod
    def get_guess(self, vector):
        """Get the next guess of the hypothesis representing
        if an attack should be made, or not

        :param vector: 2-tuple of values representing the vector

        :return: bool
        """
        pass

    @abstractmethod
    def update(self, vector, attacked, outcome):
        """Updates the hypothesis with the given
        vector which returned the given result

        :param vector: 2-tuple of values representing
        the vector

        :param attacked: bool representing if the
        vector was attacked

        :param outcome: int representing -1, 0, or 1
        representing the result from performing the
        guess on the vector
        """
        pass