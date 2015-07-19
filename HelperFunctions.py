"""This module defines some helper functions that are useful
to exist in a single place
"""
from math import sqrt
from random import random, randint

def euclidean_distance(initial_vector, to_vector):
    return sqrt(sum([(x2 - x1) ** 2 for x1, x2 in zip(initial_vector, to_vector)]))
lo
