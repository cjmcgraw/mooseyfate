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
        print ('DRPERCEPTRON: test_one: TrainedGuess: '+str(trainedGuess))
        self.assertTrue(trainedGuess==False)

    def test_attacked_good(self):
        """Test the non aggro == good case"""
        for i in range(100):
            self._hypothesis.update([1],1,1)
        trainedGuess = self._hypothesis.get_guess([1])
        print ('DRPERCEPTRON: TrainedGuess: '+str(trainedGuess))
        self.assertTrue(trainedGuess==True)



    def test_idea(self):
        """Test the perceptron idea"""
        threshold = 0.5
        learning_rate = 0.1
        weights = [0, 0, 0]
        window_size = 3
        buffer  = [1, 1, 1]
        training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]

        while True:
            error_count = 0
            for input_vector, desired_output in training_set:
                #debug print(weights)
                result = dot_product(input_vector, weights) > threshold
                error = desired_output - result
                if error != 0:
                    error_count += 1
                    for index, value in enumerate(input_vector):
                        weights[index] += learning_rate * error * value
            if error_count == 0:
                break

        """ decide on a value """
        result = dot_product(input_vector, weights) > threshold
        print('-' * 60)
        print (result)
        print('-' * 60)

        pass