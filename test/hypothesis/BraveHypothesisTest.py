"""
"""
import unittest

from src.hypothesis.BraveHypothesis import BraveHypothesis

class BraveHypothesisTest(unittest.TestCase):
    FAKE_VECTOR = [0, 0]
    WAS_ATTACKED = 1
    SUCCESSFUL_OUTCOME = 1

    def setUp(self):
        self._brave = BraveHypothesis()

    def tearDown(self):
        self._brave = None

    def test_update_fitness(self):
        self.assertEqual(0.0, self._brave.fitness())

        self._brave.update(self.FAKE_VECTOR, self.WAS_ATTACKED, self.SUCCESSFUL_OUTCOME)
        self.assertEqual(1.0, self._brave.fitness())

        self._brave.update(self.FAKE_VECTOR, self.WAS_ATTACKED, self.SUCCESSFUL_OUTCOME)
        self.assertEqual(1.0, self._brave.fitness())

        self._brave.update(self.FAKE_VECTOR, self.WAS_ATTACKED, self.SUCCESSFUL_OUTCOME)
        self.assertEqual(1.0, self._brave.fitness())

        # Add misses to the system
        self._brave.update(self.FAKE_VECTOR, 0, 0)
        self.assertEqual(0.7500, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 0, 0)
        self.assertEqual(0.6000, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 0, 0)
        self.assertEqual(0.5000, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 0, 0)
        self.assertEqual(0.4286, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 0, 0)
        self.assertEqual(0.3750, round(self._brave.fitness(), 4))

        # Add failures to the system
        self._brave.update(self.FAKE_VECTOR, 1, -1)
        self.assertEqual(0.3333, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 1, -1)
        self.assertEqual(0.3000, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, 1, -1)
        self.assertEqual(0.2727, round(self._brave.fitness(), 4))

        # Add some more hits
        self._brave.update(self.FAKE_VECTOR, self.WAS_ATTACKED, self.SUCCESSFUL_OUTCOME)
        self.assertEqual(0.3333, round(self._brave.fitness(), 4))

        self._brave.update(self.FAKE_VECTOR, self.WAS_ATTACKED, self.SUCCESSFUL_OUTCOME)
        self.assertEqual(0.3846, round(self._brave.fitness(), 4))

    def test_get_guess(self):
        for x in range(10):
            self.assertTrue(self._brave.get_guess(self.FAKE_VECTOR))
