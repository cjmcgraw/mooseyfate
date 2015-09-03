""" Note: No learn was an experiment that didn't get added into the list.
""" Idea: Create a random weighted perceptron.
""" Variations (in comments): if the fitness is bad, roll the dice again with random weights.
import random
from Hypothesis import Hypothesis

from src.lib.HelperFunctions import dot_product

class NoLearnPerceptron(Hypothesis):

    def __init__(self, windowSize=5):
        self._windowN = 0

        """ Note: _inputList is the list of inputs and the historical
                  window of inputs on which to train _weights.  Current implementation
                  is a sliding window in a modded universe defined by self._windowSize
        """
        self._windowSize = windowSize
        self._inputList =  [0] * self._windowSize
        self._inputIdx = 0
        self._inputSize = self._windowSize
        self._weightsSize = self._windowSize
        self._weights = [0] * self._weightsSize
        self._name =  "NoLearnPerceptron" + "[numInputs:" + str(self._inputSize) + "]"

        self._wins = 0;
        self._n = 1;
        self._total_wins = 0;
        self._total_n = 1;


        # tally distances
        self._distanceBetweenMistakes = 0.0
        self._meanDistanceBetweenMistakes = 0.0

        # threshold for truthyness
        self._threshold = 0.9

        # rate at which things can learn
        self._learning_rate = 0.1

        # save all interactions and add them to training
        self._training_set = []
        # don't remember everything, just the some of the prior sets inputs
        self._max_training_set_size = self._inputSize
        # our learning rate is small, here's the max amount of reps to train the neuron
        # Set this to 1 to disallow training outside of the initial error correction
        self._trainForAtLeastThisManyReps = 1

        # set weights to be random
        self._randoWeights()

    def __str__(self):
        sReturn = "NoLearnPerceptron Hypothesis: "+self._name+"\n"
        sReturn += "\tInput: "+str(self._inputList) +"\n"
        sReturn += "\tWeights: "+str(self._weights) +"\n"
        sReturn += "\tMean Distance Between Mistakes: "+str(self._meanDistanceBetweenMistakes) +"\n"
        return sReturn

    def name(self):
        return self._name

    def _train(self):
        ## Undertrain as we are limiting the reps we are trianing for
        for goWeightTraining in range(self._trainForAtLeastThisManyReps):
            error_count = 0
            #print ("DBG OptimusPERCEPTRON: _trainingset:" + str(self._training_set))
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
        return (float(self._total_wins) / float(self._total_n))

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


        # 0.)IDEA)     bogo weights / schizo-perceptron
        #    Results)  Fitness was good over short periods: when selected as a hypo, it was expectedly inconsistent
        # if (self.fitness()<0.61 and self._n>100):
        #     self._randoWeights()
        #     self._wins = 0;
        #     self._n = 1;

        # 1.) update fitness
        boolOutcome = False if outcome==-1 else True
        guess = self.get_guess(vector)

        # Monte Carlo a change in our decision based on our mistakes
        # if (self._meanDistanceBetweenMistakes > 0.0 and
        #     self._distanceBetweenMistakes >= self._meanDistanceBetweenMistakes+1):
        #     flippedCoin = random.uniform(0.0, 1.0)
        #     tails = flippedCoin > 0.3
        #     if tails and self.fitness() < 0.68:
        #         self._randoWeights()

        # check to see if we made a good decision and update wins, n, and distance between mistakes
        if guess == boolOutcome:
            self._wins += 1
            self._total_wins += self._wins
            self._distanceBetweenMistakes +=1
        else:
            self._meanDistanceBetweenMistakes = (self._distanceBetweenMistakes + self._meanDistanceBetweenMistakes ) / 2.0
            self._distanceBetweenMistakes =0
        self._n += 1
        self._total_n += self._n

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

        # IDEA)... limit the amount of chunks added with input-size padding
        # if len(self._training_set) > self._max_training_set_size:
        #     #forget some of the earlier training data
        #     for deleteWindow in range(self._inputSize):
        #         self._training_set.pop(0)

        # debug) print(str(self))

        # Variation.) update our intuition if it's bad
        # if (((self._wins/self._n)<0.65) and self._n>100):
        #     self._randoWeights()
        #     self._wins = 0;
        #     self._n = 1;

        # REMOVED for NoTrain) Don't train ... intuit
        # return self._train()
