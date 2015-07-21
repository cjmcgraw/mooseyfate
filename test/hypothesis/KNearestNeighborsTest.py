"""
"""
import unittest

from src.hypothesis.Hypothesis import KNearestNeighbors

class KNearestNeighborsTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = KNearestNeighbors(3)

    def tearDown(self):
        self._hypothesis = None

    def test_update_1dimension(self):
        # Set up cluster of two distant groups in one dimension
        for i in range(50):
            self._hypothesis.update([1], 1, -1)

        for i in range(50):
            self._hypothesis.update([50], 1, 1)

        self.assertEqual(-1, self._hypothesis.get_guess([-1]))
        self.assertEqual(-1, self._hypothesis.get_guess([1]))

        self.assertEqual(-1, self._hypothesis.get_guess([-15]))
        self.assertEqual(-1, self._hypothesis.get_guess([15]))

        self.assertEqual(-1, self._hypothesis.get_guess([-24]))
        self.assertEqual(-1, self._hypothesis.get_guess([24]))

        self.assertEqual(1, self._hypothesis.get_guess([50]))

        self.assertEqual(1, self._hypothesis.get_guess([49]))
        self.assertEqual(1, self._hypothesis.get_guess([51]))

        self.assertEqual(1, self._hypothesis.get_guess([26]))
        self.assertEqual(1, self._hypothesis.get_guess([74]))

    def test_update_2dimension(self):
        # Set up cluster of two distance groups in two dimensions
        for i in range(50):
            self._hypothesis.update([1, 1], 1, -1)

        for i in range(50):
            self._hypothesis.update([50, 50], 1, 1)

        self.assertEqual(-1, self._hypothesis.get_guess([1, 1]))
        self.assertEqual(-1, self._hypothesis.get_guess([-1, -1]))

        self.assertEqual(-1, self._hypothesis.get_guess([15, 15]))
        self.assertEqual(-1, self._hypothesis.get_guess([-15, -15]))

        self.assertEqual(-1, self._hypothesis.get_guess([24, 24]))
        self.assertEqual(-1, self._hypothesis.get_guess([-24, -24]))

        self.assertEqual(1, self._hypothesis.get_guess([50, 50]))

        self.assertEqual(1, self._hypothesis.get_guess([49, 49]))
        self.assertEqual(1, self._hypothesis.get_guess([51, 51]))

        self.assertEqual(1, self._hypothesis.get_guess([26, 26]))
        self.assertEqual(1, self._hypothesis.get_guess([74, 74]))

    def test_update_over_3dimensions(self):
        pass

    def test_fitness(self):
        pass
