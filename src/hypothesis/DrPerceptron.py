"""
"""
import random
from Hypothesis import Hypothesis

from src.lib.HelperFunctions import dot_product

class DrPerceptron(Hypothesis):

    def __init__(self, windowSize=100):
        self._name = "DrPerceptron"

        self._threshold = 0.5
        self._learning_rate = 0.1


        """ Note: _inputList is the list of inputs and the historical
                  window of inputs on which to train _weights.  Current implementation
                  is a sliding window in a modded universe defined by self._windowSize
        """
        self._windowSize = 5
        self._inputList =  [0] * self._windowSize
        self._inputIdx = 0
        self._inputSize = self._windowSize
        self._weightsSize = self._windowSize
        self._weights = [0] * self._weightsSize
        self._name = self._name + "[numInputs:" + str(self._inputSize) + "]"

        self._wins = 0;
        self._n = 1;

        self._training_set = []
        self._trainForAtLeastThisManyReps = 350

    def __str__(self):
        sReturn = "DrPerceptron Hypothesis: "+self._name+"\n"
        sReturn += "\tInput: "+str(self._inputList) +"\n"
        sReturn += "\tWeights: "+str(self._weights) +"\n"
        return sReturn

    def _train(self):
        ## Undertrain as we are limiting the reps we are trianing for
        for goWeightTraining in range(self._trainForAtLeastThisManyReps):
            error_count = 0
            #print ("DBG PERCEPTRON: _trainingset:" + str(self._training_set))
            for input_vector, desired_output in self._training_set:
                # debug print("_train: weights")
                # debug print(weights)
                result = dot_product(self._inputList, self._weights) > self._threshold
                error = desired_output - result
                if error != 0:
                    error_count += 1
                    for index, value in enumerate(self._inputList):
                        self._weights[index] += self._learning_rate * error * value
            # debug print("_train: error_count:"+str(error_count))
            # Don't overtrain
            if error_count == 0:
                break
        return True

    def _randoWeights(self):
        for idx in range (self._weightsSize) :
            self._weights[idx] = random.uniform(0.1, 0.9)
            #print('--> idx:'+str(idx)+'##'+str(self._weights[idx]))


    def _classifier(self, n):
        """
        Return true or false based on a vector
        :param n: vector to classify
        :return:
        """
        result = dot_product(self._inputList, self._weights)
        #print ("DBG PERCEPTRON: " + str(self._weights))
        #print ("DBG PERCEPTRON: " + str(result))
        boolresult =  result > self._threshold
        return boolresult

    def get_guess(self, vector):
        """
        Get the guess for a vector
        :param vector: a vector of inputs of 0 - n
        :return: boolean
        """
        return self._classifier(vector)

    def fitness(self):
        return (float(self._wins) / float(self._n))

    def update(self, vector, attacked, outcome):
        """
        Given a vector update the training matrix
        Algorithm
         # 1.) update fitness
         # 2.) add new data into a modded universe
         # 3.) add the new chunk
         # 4.) train
        :param vector: a vector of inputs of 0 - n
        :param attacked: 0 or 1
        :param outcome: -1 or 1
        :return: True
        """

        #print ("DrPerceptron Debug:  Vector:"+str(vector));
        #print ("DrPerceptron Debug:Attacked:"+str(attacked));
        #print ("DrPerceptron Debug: Outcome:"+str(outcome));

        # 1.) update fitness
        # Translate the outcome into boolean 
        boolOutcome = False if outcome==-1 else True 
        guess = self.get_guess(vector)
        # Increment wins if it's working
        if guess == boolOutcome:
            self._wins += 1
        self._n += 1

        # 2.) add new data into a modded universe
        for num in vector:
            # Note: there's a potential to set the following input to += num as a magnitude in a
            #       modded universe
            self._inputList[self._inputIdx] = num
            self._inputIdx = (self._inputIdx + 1) % self._inputSize
            #print ("DBG PERCEPTRON: INDEX" + str(+self._inputIdx))

        # 3.) add the new chunk
        training_chunk = (self._inputList, boolOutcome)
        self._training_set.append(training_chunk)


        # DEBUG 
        #print ("DrPerceptron Debug: wins:"+str(self._wins));
        #print ("DrPerceptron Debug:    n:"+str(self._n));
        #print ("DrPerceptron Debug: fitness:"+str(self.fitness()));

        # 4.) train
        return self._train()
