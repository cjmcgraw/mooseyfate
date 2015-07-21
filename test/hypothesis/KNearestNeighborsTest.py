"""Provides all unit tests for the KNN hypothesis """
import unittest

from src.hypothesis.KNearestNeighbors import KNearestNeighbors

class KNearestNeighborsTest(unittest.TestCase):

    def setUp(self):
        # We set the window to 99 to allow the first set to key
        # on 100 values updated
        self._hypothesis = KNearestNeighbors(3, window=99)

    def tearDown(self):
        self._hypothesis = None

    def test_update_1dimension(self):
        """Test the KNN algorithm in one dimension at multiple points"""
        # Set up cluster of two distant groups in one dimension
        for i in range(50):
            self._hypothesis.update([1], 1, -1)

        for i in range(50):
            self._hypothesis.update([50], 1, 1)

        self.assertFalse(self._hypothesis.get_guess([-1]))
        self.assertFalse(self._hypothesis.get_guess([1]))

        self.assertFalse(self._hypothesis.get_guess([-15]))
        self.assertFalse(self._hypothesis.get_guess([15]))

        self.assertFalse(self._hypothesis.get_guess([-24]))
        self.assertFalse(self._hypothesis.get_guess([24]))

        self.assertTrue(self._hypothesis.get_guess([50]))

        self.assertTrue(self._hypothesis.get_guess([49]))
        self.assertTrue(self._hypothesis.get_guess([51]))

        self.assertTrue(self._hypothesis.get_guess([26]))
        self.assertTrue(self._hypothesis.get_guess([74]))

    def test_update_2dimension(self):
        """Test the KNN algorithm in two dimensions at multiple points"""
        # Set up cluster of two distance groups in two dimensions
        for i in range(50):
            self._hypothesis.update([1, 1], 1, -1)

        for i in range(50):
            self._hypothesis.update([50, 50], 1, 1)

        self.assertFalse(self._hypothesis.get_guess([1, 1]))
        self.assertFalse(self._hypothesis.get_guess([-1, -1]))

        self.assertFalse(self._hypothesis.get_guess([15, 15]))
        self.assertFalse(self._hypothesis.get_guess([-15, -15]))

        self.assertFalse(self._hypothesis.get_guess([24, 24]))
        self.assertFalse(self._hypothesis.get_guess([-24, -24]))

        self.assertTrue(self._hypothesis.get_guess([50, 50]))

        self.assertTrue(self._hypothesis.get_guess([49, 49]))
        self.assertTrue(self._hypothesis.get_guess([51, 51]))

        self.assertTrue(self._hypothesis.get_guess([26, 26]))
        self.assertTrue(self._hypothesis.get_guess([74, 74]))

    def test_update_over_Ndimensions(self):
        """Test the KNN algorithm in between 2 and 100 dimensions"""
        for dimension in range(2, 100):

            # first set the aggressive monsters at [10, ..., 10]
            for i in range(50):
                self._hypothesis.update([10] * dimension, 1, -1)

            # Next set the non-aggresive monsters at [90, ..., 90]
            for i in range(50):
                self._hypothesis.update([90] * dimension, 1, 1)

            self.assertFalse(self._hypothesis.get_guess([0] * dimension))
            self.assertFalse(self._hypothesis.get_guess([40] * dimension))

            self.assertTrue(self._hypothesis.get_guess([100] * dimension))
            self.assertTrue(self._hypothesis.get_guess([55] * dimension))

    def test_fitness(self):
        pass
