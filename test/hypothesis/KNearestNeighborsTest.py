"""Provides all unit tests for the KNN hypothesis """
import unittest
from random import choice, randint

from src.hypothesis.KNearestNeighbors import KNearestNeighbors
from src.lib.TestingEnvironment import Monster

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
        """Test the KNN algorithm in between 2 and 10 dimensions"""
        for dimension in range(2, 10):

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

    def test_update_ratio_matches_expected(self):
        """Test the KNN algorithm with our built in rolling window"""
        knn = KNearestNeighbors(1)

        # First we define the method for generating our two
        # categories in a single dimension
        def generate_monster():
            color = randint(1, 100)

            # All colors less than 50 are passive
            if color < 50:
                return Monster(0, [color], 'passive')

            # Otherwise the monster is aggresive
            return Monster(1, [color], 'aggressive')

        # Run the inital training phase
        for i in range(100):
            monster = generate_monster()
            knn.update(monster.color, 1, monster.action(True))

        # Then we need to run over a set of values, we should see
        # a relatively high ratio of actual value vs maximum value
        actual_value = 0.0
        maximum_value = 5000.0

        for i in range(5000):
            monster = generate_monster()
            guess = knn.get_guess(monster.color)
            outcome = monster.action(guess)

            maximum_value -= monster._aggressive
            actual_value += outcome

            knn.update(monster.color, guess, outcome)
        
        self.assertGreaterEqual(actual_value/ maximum_value, 0.9)
