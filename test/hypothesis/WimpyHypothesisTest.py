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
        self.assertTrue(self._hypothesis.fitness()==0)
        for i in range(100):
            self._hypothesis.update([100], 1, 1)
        self.assertTrue(self._hypothesis.fitness()==1)

    def test_fitnessInHippyEnviron(self):
        """Test the WIMPY algorithm is unfit for an unaggro environ"""
        self._hypothesis = WimpyHypothesis()
        for i in range(100):
            self._hypothesis.update([100], 1, -1)
        self.assertTrue(self._hypothesis.fitness()<1)

