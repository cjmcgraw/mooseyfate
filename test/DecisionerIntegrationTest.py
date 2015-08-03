"""Provides the general integration tests that are closer
to real life scenarios of how the Hypothesis will operate
together
"""
import unittest
from random import randint, choice, random

from src.Decisioner import Decisioner
from src.hypothesis.DrPerceptron import DrPerceptron
from src.hypothesis.RandoHypothesis import RandoHypothesis
from src.hypothesis.BraveHypothesis import BraveHypothesis
from src.hypothesis.WimpyHypothesis import WimpyHypothesis
from src.hypothesis.KNearestNeighbors import KNearestNeighbors
from src.hypothesis.KMeansHypothesis import KMeansHypothesis
from src.hypothesis.SimpleProbabilityHypothesis import SimpleProbabilityHypothesis
from src.lib.TestingEnvironment import Monster, monster_generator

class DecisionerIntegrationTest(unittest.TestCase):

    def setUpDecisioner(self, *hypothesis, **kwargs):
        self.hypothesis = hypothesis
        self.decisioner = Decisioner(self.hypothesis, **kwargs)

    def tearDown(self):
        self.hypothesis = None
        self.decisioner = None

    def test_AllAggressiveMonsters_WithWimpyAndBrave(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        self.setUpDecisioner(brave, wimpy)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            monster = Monster(1, [randint(1, 100)], 'aggressive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))
            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        for i in range(5000):
            monster = Monster(1, [randint(1, 100)], 'aggressive')

            # Get the guess from the decisioner for the next 5000,
            # We expect all of them to be wimpy and thus not attack
            self.assertFalse(self.decisioner.get_guess(monster.color))

            # Then we will update from this guess
            self.decisioner.update(monster.color, 0, 0)

            # Finally we know that the wimpy hypothesis should always have
            # a greater fitness than the brave for each iteration
            self.assertGreater(wimpy.fitness(), brave.fitness())


    def test_AllPassiveMonsters_WithWimpyAndBrave(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        self.setUpDecisioner(brave, wimpy)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            monster = Monster(0, [randint(1, 100)], 'passive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))
            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        for i in range(5000):
            monster = Monster(0, [randint(1, 100)], 'aggressive')

            # Get the guess from the decisioner for the next 5000,
            # We expect all of them to be wimpy and thus not attack
            self.assertTrue(self.decisioner.get_guess(monster.color))

            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, 1)

            # Finally we know that the wimpy hypothesis should always have
            # a greater fitness than the brave for each iteration
            self.assertGreater(brave.fitness(), wimpy.fitness())

    def test_AllPassiveMonsters_WithRando(self):
        wimpy = WimpyHypothesis()
        rando = RandoHypothesis()
        self.setUpDecisioner(wimpy, rando)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            monster = Monster(0, [randint(1, 100)], 'passive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))

            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        for i in range(5000):
            monster = Monster(0, [randint(1, 100)], 'aggressive')

            self.decisioner.get_guess(monster.color)

            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, 1)

            # Flipping a coin is better than doing nothing
            self.assertGreater(rando.fitness(), wimpy.fitness())

        # Randomness should be near-even in distribution
        self.assertGreater(rando.fitness(), 0.4)
        self.assertGreater(0.6, rando.fitness())

    def test_simpleResponse_WithDrPerceptron(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        drP = DrPerceptron()
        self.setUpDecisioner(brave, wimpy, drP)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            nonAggro = 0 # this means not aggro
            color = [randint(1, 100)]
            monster = Monster(nonAggro, color, 'passive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))
            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        # DrPerceptron should converge pretty quickly and be better than wimpy but not as good as brave
        for i in range(100):
            aggro = 1 # this means aggro
            color = [randint(1, 100)]
            monster = Monster(aggro, color, 'aggressive')

            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, 1)

            self.assertGreater(drP.fitness(), wimpy.fitness())
            self.assertGreater(brave.fitness(), drP.fitness())        

    def test_frequencyResponse_WithDrPerceptron(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        drP = DrPerceptron()
        self.setUpDecisioner(brave, wimpy, drP)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            nonAggro = 0 # this means not aggro
            color = [randint(1, 100)]
            monster = Monster(nonAggro, color, 'passive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))
            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        # Dr. Perceptron should do better than brave and wimpy
        # when encountering monsters that repeat with a frequency
        # that is trainable given Dr.Perceptron's window size.
        # In otherwords, Dr. Perceptron trains on a frequency of
        # Monsters but training on a pattern is limited to the
        # input size of Dr. Perceptron (which as of this check-in
        # is 5)
        #
        # We test a staggered input
        for i in range(10):
            aggro = 1 # this means aggro
            passive = 0 # this means aggro
            evenMonstersPassive = i%2
            color = [randint(1, 100)]
            monster = Monster(evenMonstersPassive, color, 'aggressiveish')

            # Then we will update from this guess
            self.decisioner.update(monster.color, evenMonstersPassive, evenMonstersPassive)
            # drP should always be better than wimpy
            self.assertGreater(drP.fitness(), wimpy.fitness())

        # after 2 sets of 5 inputs drP should be better than brave
        self.assertGreater(drP.fitness(), brave.fitness())

    def test_frequencyResponse_forHarmonic_WithDrPerceptron(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        drP = DrPerceptron()
        self.setUpDecisioner(brave, wimpy, drP)

        # First we will start with the basic training case
        # which is the first 100 in the range
        for i in range(101):
            nonAggro = 0 # this means not aggro
            color = [randint(1, 100)]
            monster = Monster(nonAggro, color, 'passive')

            # Get the guess from the decisioner for the first 100,
            # we expect every guess to be 1
            self.assertTrue(self.decisioner.get_guess(monster.color))
            # Then we will update from this guess
            self.decisioner.update(monster.color, 1, monster.action(True))

        # Dr. Perceptron should do better than brave and wimpy
        # when encountering monsters that repeat with a frequency
        # that is trainable given Dr.Perceptron's window size.
        # In otherwords, Dr. Perceptron trains on a frequency of
        # Monsters but training on a pattern is limited to the
        # input size of Dr. Perceptron (which as of this check-in
        # is 5)
        #
        # We test a staggered input with a repeating pattern
        for i in range(1000):
            aggroPattern = [0, 1, 1, 0, 1]
            aggroIdx = i%len(aggroPattern)
            color = [randint(1, 100)]
            monster = Monster(aggroPattern[aggroIdx], color, 'aggressiveish')

            # Then we will update from this guess
            self.decisioner.update(monster.color, aggroPattern[aggroIdx], aggroPattern[aggroIdx])
            # drP should always be better than wimpy
            self.assertGreater(drP.fitness(), wimpy.fitness())

        # after a lot of training for a pattern that is harmonic within the input size Dr.P should beat out brave
        self.assertGreater(drP.fitness(), brave.fitness())
        # Since the pattern is highly regular within the input size, the fitness should be really really close to 1.
        # With great harmony results great trainability and therefore great fitness
        self.assertGreater(drP.fitness(), 0.99)
        
    def test_GroupedAggroByColor_WithWimpyBraveAndKNN(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        knn = KNearestNeighbors(3)

        self.setUpDecisioner(brave, wimpy, knn)

        def create_monster():
            color = randint(1, 100)

            # Every monster below 50 is aggressive
            if color < 50:
                return Monster(1, [color], 'aggressive')
            # Otherwise if they are above 50 they are
            # passive
            else:
                return Monster(0, [color], 'passive')

        # Next we load up the training data
        for i in range(100):
            # Create the monster and generate all the data, by default
            # we expect everything in the training period to be true
            # meaning attack for data
            monster = create_monster()
            self.assertTrue(self.decisioner.get_guess(monster.color))
            self.decisioner.update(monster.color, 1, monster.action(True))

        # Finally we need to know that normal KNN was matched as the best
        # fitness for the data set
        self.assertGreater(knn.fitness(), brave.fitness())
        self.assertGreater(knn.fitness(), wimpy.fitness())

        # Then we are going to run over all of the data sets
        # We want to also track the actual value and the maximum
        # value for comparison
        maximum_value = 5000.0
        actual_value = 0.0

        for i in range(5000):
            # Create the monster, guess on it and grab the outcome
            # which is all required information for the loop
            monster = create_monster()
            guess = self.decisioner.get_guess(monster.color)
            outcome = monster.action(guess)

            # update values for comparison after loop
            maximum_value -= monster._aggressive
            actual_value += outcome

            # 
            self.decisioner.update(monster.color, guess, outcome)

            # We need to know that KNN is still our best fit for this
            # data set
            self.assertGreater(knn.fitness(), brave.fitness())
            self.assertGreater(knn.fitness(), wimpy.fitness())

        # Finally we expect that the standard KNN process will obtain
        # within 10 percent margin of the best possible solution
        self.assertGreater(actual_value / maximum_value, 0.9)

    def test_GroupAggroByColorAndProbability_WithWimpyBraveKNNAndKMeans(self):
        brave = BraveHypothesis()
        wimpy = WimpyHypothesis()
        knn = KNearestNeighbors(3)

        kmeans = KMeansHypothesis(1, 2, [SimpleProbabilityHypothesis() for x in range(2)])

        self.setUpDecisioner(brave, wimpy, knn, kmeans)

        def create_monster():
            p_values = [0.3, 0.4, 0.6, 0.2]
            base = choice([20, 80])
            color = base + randint(-5, 5)

            if base == 20:
                if random() <= p_values[0]:
                    return Monster(0, [color], 'passive')
                return Monster(1, [color], 'aggressive')
            if base == 40:
                if random() <= p_values[1]:
                    return Monster(0, [color], 'passive')
                return Monster(1, [color], 'aggressive')
            if base == 60:
                if random() <= p_values[2]:
                    return Monster(0, [color], 'passive')
                return Monster(1, [color], 'aggressive')
            if base == 80:
                if random() <= p_values[3]:
                    return Monster(0, [color], 'passive')
                return Monster(1, [color], 'aggressive')

        # Lets train against some monsters for the standard initial training
        # period
        for x in range(1000):
            monster = create_monster()
            outcome = monster.action(True)
            self.decisioner.update(monster.color, True, outcome)

            kmeans_guess = kmeans.get_guess(monster.color)

            print('Brave fitness = ' + str(brave.fitness()))
            print('Wimpy fitness = ' + str(wimpy.fitness()))
            print('KNN fitness = ' + str(knn.fitness()))
            print('KMeans fitness = ' + str(kmeans.fitness()))
            print('vector =' + str(monster.color))
            print('KMeans Guess = ' + str(kmeans_guess))
            print(kmeans._centroids)
            print(vars(kmeans._sub_hypothesis[0]))
            print(vars(kmeans._sub_hypothesis[1]))
            print('')

        # Now we have trained our data set, we need to get some guesses
