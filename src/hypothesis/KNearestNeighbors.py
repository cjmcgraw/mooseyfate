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

    def name(self):
        return "KNearestNeighbors (k=" + str(self._k) + ")"

    def get_guess(self, vector):
        # If we haven't obtained atleast k values of
        # our window then we should use true instead
        if len(self._training_data) < self._k:
            return True

        # grab the k nearest neighbors using euclidean
        # distance
        dist = lambda x: euclidean_distance(vector, x[1])
        closest_points = nsmallest(self._k, enumerate(self._training_data), key=dist)
        closest_labels = [self._training_labels[i] for (i, pt) in closest_points]
        return max(set(closest_labels), key=closest_labels.count)

    def update(self, vector, attacked, outcome):
        super(KNearestNeighbors, self).update(vector, attacked, outcome)

        # If we are in our training window then we
        # should train up our data
        if len(self._training_data) <= self._window:
            if attacked:
                self._training_data.append(vector)
                self._training_labels.append(outcome == 1)
