"""Provides all unit tests for the KNN hypothesis """
import unittest
from random import choice, randint

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

    def test_update_rolling_window(self):
        """Test the KNN algorithm with our built in rolling window"""
        # First we create a set of beginning data to pass the 99 window
        # into the first iteration
        for i in range(50):
            # the cluster around 10 will be aggressive
            self._hypothesis.update([10] * 5, 1, -1)

        for i in range(50):
            # the cluster around 50 will be passive
            self._hypothesis.update([50] * 5, 1, 1)

        # Asserts to validate its working as expected
        self.assertFalse(self._hypothesis.get_guess([20] * 5))
        self.assertTrue(self._hypothesis.get_guess([40] * 5))

        # Next we provide an entirely new set of data
        # for the next window. Ideally it should shift
        # to using the data set
        for i in range(50):
            # we will simply swap the aggression for each loop
            self._hypothesis.update([10] * 5, 1, 1)

        for i in range(50):
            self._hypothesis.update([50] * 5, 1, -1)

        # Finally we assert that the same previous calls
        # now give the updated data. Therefore showing that
        # the algorithm is now using the shifted value
        self.assertTrue(self._hypothesis.get_guess([20] * 5))
        self.assertFalse(self._hypothesis.get_guess([40] * 5))

    def test_fitness_second_window_and_third_window(self):
        """Test the KNN Algorithm in the first window moving to the second and
        third"""

        # First we are going to have everything less than 50 be aggressive
        # and everything greater than 50 passive
        for x in range(50):
            vector = [randint(1, 50) for i in range(5)]
            self._hypothesis.update(vector, 1, -1)

        for x in range(50):
            vector = [randint(50, 100) for i in range(5)]
            self._hypothesis.update(vector, 1, 1)

        # Now we expect our fitness to be relatively high
        # I will check this by determining the error of the
        # fitness from 0.95
        err = abs(0.95 - self._hypothesis.fitness())
        self.assertGreaterEqual(0.05, err)

        # Guessing around 25 should yield us "False" for
        # if we should attack
        self.assertFalse(self._hypothesis.get_guess([25] * 5))

        # Guessing around 75 should yield us "True" for
        # if we should attack
        self.assertTrue(self._hypothesis.get_guess([75] * 5))

        # Then we are going to flip the aggression
        # hopefully the third window will be able to
        # adjust accordingly
        for x in range(50):
            vector = [randint(1, 50) for i in range(5)]
            self._hypothesis.update(vector, 1, 1)

        for x in range(50):
            vector = [randint(50, 100) for i in range(5)]
            self._hypothesis.update(vector, 1, -1)

        # Finally we expect the new fitness to be high even
        # though the classification is exactly the opposite
        # of the second window
        err = abs(0.95 - self._hypothesis.fitness())
        self.assertGreaterEqual(0.05, err)

        # Guessing around 25 should yield us "True" now
        self.assertTrue(self._hypothesis.get_guess([25] * 5))

        # And guessing around 75 should yield us "False"
        self.assertFalse(self._hypothesis.get_guess([75] * 5))
