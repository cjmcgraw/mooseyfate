"""Hypothesis module defines the Hypothesis abstract class """

from abc import ABCMeta, abstractmethod

class Hypothesis:
    """Defines the Hypothesis required methods"""

    __metaclass__ = ABCMeta

    def __init__(self):
        self._success = 0.0
        self._n = 0.0

    def fitness(self):
        """Retrieves a float representing the fitness of
        this hypothesis to its previous data

        :return: float
        """
        if self._n < 1:
            return 0.0
        return self._success / self._n

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

        First we define some of our terms

        let:
            success = the number of correct guesses made
            n = the number of guesses made where information was gathered

            guess = the guess that this hypothesis would have made
            attacked = the actual guess made (whether this hypothesis or not)
            outcome = the outcome of making the attacked guess

        By virtue of the problem there are certain conditions
        in which it makes sense to increment the successes and n
        other times to increment only the n, and a third case
        in which it makes sense to do nothing.

        We have the following potential cases for all values,
        excluding vector.

        guess (the hypothesis made guess): [1, 0] (true, false)
        attacked: [1, 0] (true, false, of the actual hypothesis that guessed)
        outcome: [1, 0, -1] (representing passive, unknown, and aggressive)

        using a bit of simple combinatorics we get the following
        table of potential values

            guess   attacked    outcome
            ===========================
            1       1           1
            1       1           0
            1       1           -1
            1       0           1
            1       0           0
            1       0           -1
            0       1           1
            0       1           0
            0       1           -1
            0       0           1
            0       0           0
            0       0           -1
            ===========================

        So when we do not attack monsters we automatically get a '0'
        outcome. Because of this we know then we can ignore any values
        that have a zero attacked and a non-zero outcome.

        Furthermore we know that we cannot get a zero outcome if we performed
        an attack. As such we can also exclude all rows where the attacked
        is zero and the outcome is non-zero.

        This leads us to the following updated table:

            guess   attacked    outcome
            ===========================
            1       1           1
            1       1           -1
            1       0           0
            0       1           1
            0       1           -1
            0       0           0
            ===========================

        Now if we group each row by their relationship to being a
        'win', a 'lose', and a 'no information' we get the following

            win:    [1, 1, 1], [0, 1, -1]

            lose:   [1, 1, -1], [0, 1, 1]

            no/info:[1, 0, 0], [0, 0, 0]

        From this we can determine what we should do in each
        situation:

            win: increment success, increment n

            lose: increment n

            no/info: do nothing

        from this we can extrapolate how the update should
        generally track the fitness for any given hypothesis
        """
        guess = self.get_guess(vector)

        # If we know we attacked, then at the very least we need
        # to increment n as seen by the above comment
        if attacked != 0:
            self._n += 1

            # Given that we attacked, if our guess and the
            # attacked are the same, and the outcome is positive
            # we can increment our successes
            if guess == attacked and outcome > 0:
                self._success += 1

            # Otherwise if the guess does not equal attacked and 
            # the outcome is negative we want to increment our
            # successes as well
            if guess != attacked and outcome < 0:
                self._success += 1
