"""Hypothesis module defines the Hypothesis abstract class """

from Hypothesis import Hypothesis
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

class LogRegressionHypothesis:
    """Defines the Hypothesis required methods"""

    def __init__(self):
        self._success = 0.0
        self._n = 0.0

    def get_guess(self, vector):
        """Get the next guess of the hypothesis representing
        if an attack should be made, or not

        :param vector: 2-tuple of values representing the vector

        :return: bool
        """
        pass

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

            win:    [1, 1, 1], [0, 1, -1]

            lose:   [1, 1, -1], [0, 1, 1]

            no/info:[1, 0, 0], [0, 0, 0]

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
