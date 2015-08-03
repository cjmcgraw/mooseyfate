"""Provides the general integration tests that are closer
to real life scenarios of how the Hypothesis will operate
together
"""
import unittest
from random import randint

from src.Decisioner import Decisioner
from src.hypothesis.BraveHypothesis import BraveHypothesis
from src.hypothesis.WimpyHypothesis import WimpyHypothesis
from src.hypothesis.KNearestNeighbors import KNearestNeighbors
from src.hypothesis.KMeansHypothesis import KMeansHypothesis
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
            self.assertTrue(self.decisioner.should_attack(monster.color))
            # Then we will learn from this guess
            self.decisioner.learn(monster.color, 1, monster.action(True))

        for i in range(5000):
            monster = Monster(1, [randint(1, 100)], 'aggressive')

            # Get the guess from the decisioner for the next 5000,
            # We expect all of them to be wimpy and thus not attack
            self.assertFalse(self.decisioner.should_attack(monster.color))

            # Then we will learn from this guess
            self.decisioner.learn(monster.color, 0, 0)

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
            self.assertTrue(self.decisioner.should_attack(monster.color))
            # Then we will learn from this guess
            self.decisioner.learn(monster.color, 1, monster.action(True))

        for i in range(5000):
            monster = Monster(0, [randint(1, 100)], 'aggressive')

            # Get the guess from the decisioner for the next 5000,
            # We expect all of them to be wimpy and thus not attack
            self.assertTrue(self.decisioner.should_attack(monster.color))

            # Then we will learn from this guess
            self.decisioner.learn(monster.color, 1, 1)

            # Finally we know that the wimpy hypothesis should always have
            # a greater fitness than the brave for each iteration
            self.assertGreater(brave.fitness(), wimpy.fitness())

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
            self.assertTrue(self.decisioner.should_attack(monster.color))
            self.decisioner.learn(monster.color, 1, monster.action(True))

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
            guess = self.decisioner.should_attack(monster.color)
            outcome = monster.action(guess)

            # update values for comparison after loop
            maximum_value -= monster._aggressive
            actual_value += outcome

            # 
            self.decisioner.learn(monster.color, guess, outcome)

            # We need to know that KNN is still our best fit for this
            # data set
            self.assertGreater(knn.fitness(), brave.fitness())
            self.assertGreater(knn.fitness(), wimpy.fitness())

        # Finally we expect that the standard KNN process will obtain
        # within 10 percent margin of the best possible solution
        self.assertGreater(actual_value / maximum_value, 0.9)
