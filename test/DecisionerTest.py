"""
"""
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
        self.decisioner = Decisioner(self.mocks)

    def tearDown(self):
        self.mocks = None
        self.decisioner = None

    def test_should_attack(self):
        """Tests the 'should_attack' method of the Decisioner"""

        # Set up the first mock to be selected for the guess
        self.mocks[0]._fitness = 0.71
        self.mocks[0]._next_guess = True

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertTrue(response)

        self.mocks[0]._next_guess = False

        # Set up the second mock to be selected for the guess
        self.mocks[1]._fitness = 0.72
        self.mocks[1]._next_guess = True

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertTrue(response)

        self.mocks[1]._next_guess = False

        # Set up the third mock to be selected for the guess
        self.mocks[2]._fitness = 0.73
        self.mocks[2]._next_guess = True

        response = self.decisioner.should_attack(self.FAKE_VECTOR)
        self.assertTrue(response)

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
