import unittest
from src.hypothesis.WimpyHypothesis import WimpyHypothesis

class KNearestNeighborsTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = WimpyHypothesis()

    def tearDown(self):
        self._hypothesis = None

    def test_initGuess(self):
        """Test the WIMPY algorithm initializes guess to zero"""
        self.assertFalse(self._hypothesis.get_guess([1]))

    def test_fitnessInAggroEnviron(self):
        """Test the WIMPY algorithm is fit for an aggro environ"""
        self.assertEquals(0, self._hypothesis.fitness())
        for i in range(100):
            self._hypothesis.update([100], 1, 1)
        self.assertEquals(0.0, self._hypothesis.fitness())

    def test_fitnessInHippyEnviron(self):
        """Test the WIMPY algorithm is unfit for an unaggro environ"""
        self._hypothesis = WimpyHypothesis()
        for i in range(100):
            self._hypothesis.update([100], 1, -1)
        self.assertEquals(1.0, self._hypothesis.fitness())

