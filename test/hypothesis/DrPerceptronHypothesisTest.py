import unittest
from src.hypothesis.DrPerceptron import DrPerceptron
from src.lib.HelperFunctions import dot_product

class DrPerceptronHypothesisTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = DrPerceptron()

    def tearDown(self):
        self._hypothesis = None

    def test_attacked_bad(self):
        """Test the aggro == bad case"""
        for i in range(100):
            self._hypothesis.update([1],1,-1)
        trainedGuess = self._hypothesis.get_guess([1])
        print ('DRPERCEPTRON: test_attacked_bad TrainedGuess: '+str(trainedGuess))
        print (str(self._hypothesis))
        self.assertTrue(trainedGuess==False)

    def test_attacked_good(self):
        """Test the non aggro == good case"""
        for i in range(100):
            self._hypothesis.update([1],1,1)
        trainedGuess = self._hypothesis.get_guess([1])
        print ('DRPERCEPTRON: test_attacked_good TrainedGuess: '+str(trainedGuess))
        print (str(self._hypothesis))
        self.assertTrue(trainedGuess==True)

    def test_attacked_bad_randoWeights(self):
        """Randomize the weights: Test the aggro == bad case"""
        self._hypothesis._randoWeights()
        for i in range(100):
            self._hypothesis.update([1],1,-1)
        trainedGuess = self._hypothesis.get_guess([1])
        #print ('DRPERCEPTRON: test_attacked_bad TrainedGuess: '+str(trainedGuess))
        print (str(self._hypothesis))
        self.assertTrue(trainedGuess==False)

    def test_attacked_good_randoWeights(self):
        """Randomize the weights: Test the non aggro == good case"""
        self._hypothesis._randoWeights()
        for i in range(100):
            self._hypothesis.update([1],1,1)
        trainedGuess = self._hypothesis.get_guess([1])
        #print ('DRPERCEPTRON: test_attacked_good TrainedGuess: '+str(trainedGuess))
        print (str(self._hypothesis))
        self.assertTrue(trainedGuess==True)

