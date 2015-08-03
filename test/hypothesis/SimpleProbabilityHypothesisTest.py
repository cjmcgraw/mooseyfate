"""
"""
import unittest
from random import random, randint

from src.lib.TestingEnvironment import Monster
from src.hypothesis.SimpleProbabilityHypothesis import SimpleProbabilityHypothesis

def create_monster(p):
    if random() <= p:
        return Monster(0, [randint(1, 100)], 'passive')
    return Monster(1, [randint(1, 100)], 'aggressive')

class SimpleProbabilityHypothesisTest(unittest.TestCase):

    def setUp(self):
        self.hypothesis = SimpleProbabilityHypothesis()

    def tearDown(self):
        self.hypothesis = None

    def test_half_probability(self):
        self.run_tests_probability_p(0.99)

    def run_tests_probability_p(self, p):
        # Train inital period
        for i in range(100):
            monster = create_monster(p)
            self.hypothesis.update(monster.color, 1, monster.action(True))

        for x in range(500):
            monster = create_monster(p)
            guess = self.hypothesis.get_guess(monster.color)
            outcome = monster.action(guess)
            self.hypothesis.update(monster.color, guess, outcome)

        err = abs(self.hypothesis.p_value() - p)
        self.assertGreater(0.05, err)
