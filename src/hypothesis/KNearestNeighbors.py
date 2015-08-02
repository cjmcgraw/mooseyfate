"""
"""
from heapq import nsmallest

from src.lib.HelperFunctions import euclidean_distance
from src.hypothesis.Hypothesis import Hypothesis

class KNearestNeighbors(Hypothesis):

    def __init__(self, k, window=100):
        super(KNearestNeighbors, self).__init__()
        self._window = window

        self._training_data = []
        self._training_labels = []

        self._k = k
        self._classifier = lambda x: True

        self._next_n = 0.0
        self._next_success = 0.0

    def _create_classifier(self):
        data = self._training_data
        labels = self._training_labels
        def classify(vector):
            dist = lambda x: euclidean_distance(vector, x[1])
            closest_points = nsmallest(self._k, enumerate(data), key=dist)
            closest_labels = [labels[i] for (i, pt) in closest_points]
            return max(set(closest_labels), key=closest_labels.count)
        return classify

    def get_guess(self, vector):
        return self._classifier(vector)

    def update(self, vector, attacked, outcome):
        super(KNearestNeighbors, self).update(vector, attacked, outcome)
        if outcome == 1:
            result = True
        else:
            result = False

        if attacked:
            self._training_data.append(vector)
            self._training_labels.append(result)

        if len(self._training_data) > self._window:
            self._classifier = self._create_classifier()
            self._training_data = []
            self._training_labels = []

            # Then we override the old fitness data
            # with the new fitness data
            self._n = self._next_n
            self._success = self._next_success

            self._next_n = 0.0
            self._next_success = 0.0
        else:
            self.track_fitness_for_next_classification(vector, attacked, outcome)
    def track_fitness_for_next_classification(self, vector, attacked, outcome):
        # If we have more then 10 data points then we may
        # have enough informatino to begin recording the
        # fitness for the next classify iteration
        if len(self._training_data) > 20:

            # Create the next classify function
            next_classify = self._create_classifier()
            # grab the guess from the function
            guess = next_classify(vector)

            # Update normally as if it were the classification
            # that we are currently on, but save the data to
            # the 'next' classification, that way the fitness
            # can be updated when we reach the point
            if attacked != 0:
                self._next_n += 1

                if guess == attacked and outcome > 0:
                    self._next_success += 1

                if guess != attacked and outcome < 0:
                    self._next_success += 1
