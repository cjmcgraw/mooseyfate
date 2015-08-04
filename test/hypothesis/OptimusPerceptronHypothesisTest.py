import unittest

from src.hypothesis.OptimusPerceptron import OptimusPerceptron

class OptimusPerceptronHypothesisTest(unittest.TestCase):

    def setUp(self):
        self._hypothesis = OptimusPerceptron()

    def tearDown(self):
        self._hypothesis = None

    def test_attacked_bad(self):
        """Perceptron: Test the aggro == bad case"""
        for i in range(100):
            self._hypothesis.update([1],1,-1)
        trainedGuess = self._hypothesis.get_guess([1])
        #print ('DRPERCEPTRON: test_attacked_bad TrainedGuess: '+str(trainedGuess))
        #print (str(self._hypothesis))
        self.assertTrue(trainedGuess==False)

    def test_attacked_good(self):
        """Perceptron: Test the non aggro == good case"""
        for i in range(100):
            self._hypothesis.update([1],1,1)
        trainedGuess = self._hypothesis.get_guess([1])
        #print ('DRPERCEPTRON: test_attacked_good TrainedGuess: '+str(trainedGuess))
        #print (str(self._hypothesis))
        self.assertTrue(trainedGuess==True)

    def test_attacked_bad_randoWeights(self):
        """Perceptron: Randomize the weights: Test the aggro == bad case"""
        self._hypothesis._randoWeights()
        for i in range(100):
            self._hypothesis.update([1],1,-1)
        trainedGuess = self._hypothesis.get_guess([1])
        print ('OptimusPERCEPTRON: test_attacked_bad TrainedGuess: '+str(trainedGuess))
        print (str(self._hypothesis))
        self.assertTrue(trainedGuess==False)

    def test_attacked_good_randoWeights(self):
        """Perceptron: Randomize the weights: Test the non aggro == good case"""
        self._hypothesis._randoWeights()
        for i in range(100):
            self._hypothesis.update([1],1,1)
        trainedGuess = self._hypothesis.get_guess([1])
        #print ('DRPERCEPTRON: test_attacked_good TrainedGuess: '+str(trainedGuess))
        #print (str(self._hypothesis))
        self.assertTrue(trainedGuess==True)

