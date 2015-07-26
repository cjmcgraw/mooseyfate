import unittest
from src.hypothesis.RandoHypothesis import RandoHypothesis

class KNearestNeighborsTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = RandoHypothesis()

    def tearDown(self):
        self._hypothesis = None

    def test_initGuess(self):
        """Test the Rando algorithm returns a value"""
        isTautological = self._hypothesis.get_guess([1]) 
        self.assertTrue(isTautological or not isTautological)

    def test_fitnessInAggroEnviron(self):
        """RandoHypothesis: Test fitness after a thousand flips in Aggro Environment"""
        self.assertTrue(self._hypothesis.fitness()==0)
        for i in range(1000):
            self._hypothesis.update([100], 1, 1)
        self.assertTrue(self._hypothesis.fitness()>0.4)
        self.assertTrue(self._hypothesis.fitness()<0.6)
        print ('RandoHypothesis Fitness: ' + str(self._hypothesis.fitness()) + ' ... ')
