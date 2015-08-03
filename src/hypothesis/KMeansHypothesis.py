"""This module represents the hypothesis that the
monsters are split into means that are capable of being
determined
"""
from random import randint

from src.lib.HelperFunctions import euclidean_distance
from Hypothesis import Hypothesis

class KMeansHypothesis(Hypothesis):

    def __init__(self, dim, k, sub_hypothesis):
        super(KMeansHypothesis, self).__init__()
        self.initialize_state(dim, k, sub_hypothesis)

    def initialize_state(self, dim, k, sub_hypothesis):
        self._centroids = [[randint(1, 100) for d in range(dim)] for x in range(k)]
        self._points = {i : [] for i in range(k)}
        self._sub_hypothesis = sub_hypothesis

    def getName(self):
        return "KMeansHypothesis"

    def get_guess(self, vector):
        index = self.index_of_nearest_centroid(vector)
        return self._sub_hypothesis[index].get_guess(vector)

    def update(self, vector, attacked, outcome):
        super(KMeansHypothesis, self).update(vector, attacked, outcome)
        
        for hyp in self._sub_hypothesis:
            hyp.update(vector, attacked, outcome)

        index = self.index_of_nearest_centroid(vector)
        self._points[index].append(vector)
        self._centroids[index] = [sum(xi) / len(xi) for xi in zip(*self._points[index])]

    def index_of_nearest_centroid(self, vector):
        dist = lambda v: euclidean_distance(v[1], vector)
        return min(enumerate(self._centroids), key=dist)[0]
