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


