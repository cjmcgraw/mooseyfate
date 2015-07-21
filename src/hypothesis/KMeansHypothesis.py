"""This module represents the hypothesis that the
monsters are split into means that are capable of being
determined
"""
from random import randint

from src.lib.HelperFunctions import euclidean_distance
from Hypothesis import Hypothesis

class KMeansHypothesis(Hypothesis):

    def __init__(self, dim, k):
        self._centroids = [[randint(1, 100) for d in range(dim)] for x in range(k)]
        self._points = {i : [] for i in range(k)}

    def getName(self):
        return "KMeansHypothesis"

    def fitness(self):
        pass

    def get_guess(self, vector):
        pass

    def update(self, vector, attacked, outcome):
        distance = lambda v: euclidean_distance(v[1], vector)
        index = min(enumerate(self._centroids), key=distance)[0]
        self._points[index].append(vector)
        self._centroids[index] = [sum(xi) / len(xi) for xi in zip(*self._points[index])]
