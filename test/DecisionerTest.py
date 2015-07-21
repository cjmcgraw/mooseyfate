"""Provies the unit tests for the decisioner which acts as the central unit
through which hypothesis are chosen """
import unittest

from test.hypothesis.MockHypothesis import MockHypothesis

from src.Decisioner import Decisioner

class DecisionerTest(unittest.TestCase):
    FAKE_VECTOR = [0, 0]
    FAKE_ACTION = 1
    FAKE_OUTCOME = 1

    def setUp(self):
        self.mocks = [MockHypothesis(fitness=0.5),
                      MockHypothesis(fitness=0.6),
                      MockHypothesis(fitness=0.7)]
        self.decisioner = Decisioner(self.mocks, training_window=0)

    def tearDown(self):
        self.mocks = None
        self.decisioner = None

    def test_should_attack(self):
        """Tests the 'should_attack' method of the Decisioner"""

        # Set up the first mock to be selected for the guess
        self.mocks[0]._fitness = 0.71
        self.mocks[0]._next_guess = 'first'

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertEqual('first', response)

        # Set up the second mock to be selected for the guess
        self.mocks[1]._fitness = 0.72
        self.mocks[1]._next_guess = 'second'

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertEqual('second', response)

        # Set up the third mock to be selected for the guess
        self.mocks[2]._fitness = 0.73
        self.mocks[2]._next_guess = 'third'

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertEqual('third', response)

    def test_should_attack_training_window(self):
        """Tests the 'should_attack' method of the decisioner with the
        training window in place"""

        # First we know need to create a new decisioner with a new
        # training window
        decisioner = Decisioner(self.mocks, training_window=100)

        # Then we test that we are receiving true while in the window
        for i in range(100):
            self.assertTrue(decisioner.should_attack(self.FAKE_VECTOR))
            decisioner.learn(self.FAKE_VECTOR, self.FAKE_ACTION, self.FAKE_OUTCOME)

        # Finally now that we've exceeded the window we test that we
        # are actually getting hypothesis that are chosen
        self.mocks[0]._fitness = 0.99
        self.mocks[0]._next_guess = 'spam'

        response = decisioner.should_attack(self.FAKE_VECTOR)

        self.assertEqual('spam', response)

    def test_learn(self):
        """Tests the 'learn' method of the Decisioner"""

        # we simply need to update multiple times. So we try
        # it here 10 times total
        for i in range(10):
            # Call the learn method
            self.decisioner.learn(self.FAKE_VECTOR, self.FAKE_ACTION, self.FAKE_OUTCOME)

            # Check that the hypothesis all have been updated
            for hypothesis in self.mocks:
                self.assertEqual(i + 1, hypothesis._times_updated)

if __name__ == '__main__':
    unittest.main()
