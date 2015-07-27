"""Provides all unit tests for the KMeans hypothesis """
import unittest
from itertools import combinations
from random import randint, choice

from test.hypothesis.MockHypothesis import MockHypothesis
from src.hypothesis.KMeansHypothesis import KMeansHypothesis

class KMeansHypothesisTest(unittest.TestCase):

    def set_state_with_k_centroids(self, k, dim=3):
        self._sub_h = [MockHypothesis(i) for i in range(k)]
        self._hypothesis = KMeansHypothesis(dim, k, self._sub_h)

    def tearDown(self):
        self._sub_h = None
        self._hypothesis = None

    def test_update_and_get_guess_two_centroids(self):
        """Tests the update and get guess with two centroids"""
        # Set up initial conditions
        self.set_state_with_k_centroids(2)

        # Set up the initial centroids
        c1 = (25, 25, 25)
        c2 = (75, 75, 75)


        # Train the centroids
        self.train_hypothesis_with_centroids(c1, c2, maximum_shift=15)

        # Now lets get some guesses that should be near our
        # centroids

        # Now since the initial centroids are chosen randomly we cannot
        # be certain which hypothesis will be chosen for them. As such
        # we will have to work under the initial assumption that the
        # system has foun the exactly specified centroids and then
        # extrapolate from that
        c1_index = self._hypothesis.get_guess(c1)
        c2_index = self._hypothesis.get_guess(c2)

        # Then we need to know that the system found two separrate  centroids
        # for each of the actual centroids
        self.assertNotEqual(c1_index, c2_index)

        # First we try to check the index of the vectors near the
        # first centroid. We expect anything beneath (50, 50, 50)
        # to, ideally, map to the first centroid
        self.assertEqual(c1_index, self._hypothesis.get_guess((25, 25, 25)))
        self.assertEqual(c1_index, self._hypothesis.get_guess((0, 0, 0)))
        self.assertEqual(c1_index, self._hypothesis.get_guess((40, 40, 40)))

        # Second we try to check the index of the vectors near the
        # second centroid. We expect anything above (50, 50, 50)
        # to, ideally, map to the second centroid
        self.assertEqual(c2_index, self._hypothesis.get_guess((75, 75, 75)))
        self.assertEqual(c2_index, self._hypothesis.get_guess((100, 100, 100)))
        self.assertEqual(c2_index, self._hypothesis.get_guess((60, 60, 60)))

    def test_update_and_get_guess_three_centroids(self):
        """Tests the update and get guess with two centroids"""
        # Set up initial conditions
        self.set_state_with_k_centroids(3)

        # Set up the initial centroids
        c1 = (-50, -50, -50)
        c2 = (50, 50, 50)
        c3 = (150, 150, 150)


        # Train the centroids
        self.train_hypothesis_with_centroids(c1, c2, c3, maximum_distance=25)

        # Now lets get some guesses that should be near our
        # centroids

        # Now since the initial centroids are chosen randomly we cannot
        # be certain which hypothesis will be chosen for them. As such
        # we will have to work under the initial assumption that the
        # system has found the exactly specified centroids and then
        # extrapolate from that
        c1_index = self._hypothesis.get_guess(c1)
        c2_index = self._hypothesis.get_guess(c2)
        c3_index = self._hypothesis.get_guess(c3)

        # Assert that all of the found centroids have unique indices
        for ci, cx in combinations([c1_index, c2_index, c3_index], 2):
            self.assertNotEqual(ci, cx)

        for centroid_index, centroid in zip([c1_index, c2_index, c3_index], [c1, c2, c3]):
            for x in range(10):
                vector = self.find_vector_close_to(centroid, maximum_distance=25)
                self.assertEqual(centroid_index, self._hypothesis.get_guess(vector))



    def train_hypothesis_with_centroids(self, *centroids, **kwargs):
        for centroid in centroids:
            for i in range(int(100 / len(centroids))):
                self._hypothesis.update(self.find_vector_close_to(centroid, kwargs.get('maximum_distance', 10)), 1, 1)

    def find_vector_close_to(self, centroid, maximum_distance=10):
        result = []

        for xi in centroid:
            d = randint(0, maximum_distance)
            result.append(xi + choice([-1, 1]) * d)
            maximum_distance -= d

        return tuple(result)

