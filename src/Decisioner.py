"""Decisioner module defines the Decisioner class and the main
method for running the decision framework
"""
from src.hypothesis.Hypothesis import Hypothesis

class Decisioner(Hypothesis):
    """Decisioner class retrieves monsters, finds the best hypothesis
    to use, executes the guess from the hypothesis and then updates all
    the hypothesis.

    The following algorithm is used in this decisioner:

        1. Get current state (retrieve monster)
        2. Select best fitting Hypothesis
        3. Get guess from best fitting Hypothesis
        4. Perform the guess (act on the monster)
        5. Update all Hypothesis with the result
    """

    def __init__(self, hypothesis, training_window=101, trace=False):
        """Initializes the Decisioner """
        self.all_hypothesis = hypothesis
        self._window = training_window
        self._trace = trace

    def println(self, msg):
        if(self._trace):
            print(msg)

    def name(self):
        return "Decisioner: " + self.get_best_fit_hypothesis().name()

    def fitness(self):
        return self.get_best_fit_hypothesis().fitness()

    def get_best_fit_hypothesis(self):
        """Gets the hypothesis that is the best fit

        :return: Hypothesis class
        """
        hyp = sorted(self.all_hypothesis, key=lambda h: h.fitness(), reverse=True)
        self.println("All fitnesses in expected order and by class")
        for h in hyp:
            self.println(h.name() +  ' = ' + str(h.fitness()))
        self.println('')
        return hyp[0]


    def get_guess(self, vector):
        """Retrieves a boolean value representing if the given
        monster should be attacked

        :param vector: 2-tuple representing the monster to
        be decided on

        :return: bool
        """
        self.println("Getting guess for vector: " + str(list(vector)))
        if self._window > 0:
            return True
        best_hypothesis = self.get_best_fit_hypothesis()
        guess = best_hypothesis.get_guess(vector)

        self.println("Best fit hypothesis: " + str(best_hypothesis.name()))
        self.println("Guess: " + str(guess))
        self.println('')

        return guess

    def update(self, vector, attacked, outcome):
        """Applies the given monster-vector and outcome
        to the hypothesis

        :param vector: 2-tuple representing the monster-vector

        :param attacked: bool representing if the monster-vector
        was attacked

        :param outcome: int representing if the outcome of
        acting on the vector
        """
        self.println("Learning on vector: " + str(list(vector)))
        self.println("Was the vector attacked?: " + str(attacked))
        self.println("What what the outcome of the action?: " + str(outcome))
        self.println('')
        for hypothesis in self.all_hypothesis:
            hypothesis.update(vector, attacked, outcome)
        self._window -= 1

if __name__ == "__main__":
    from random import randint, random
    from src.lib.TestingEnvironment import Monster

    from src.hypothesis.BraveHypothesis import BraveHypothesis
    from src.hypothesis.WimpyHypothesis import WimpyHypothesis
    from src.hypothesis.KNearestNeighbors import KNearestNeighbors
    from src.hypothesis.DrPerceptron import DrPerceptron
    from src.hypothesis.OptimusPerceptron import OptimusPerceptron
    from src.hypothesis.SimpleProbabilityHypothesis import SimpleProbabilityHypothesis
    from src.hypothesis.RandoHypothesis import RandoHypothesis


    def create_monster():
        color = randint(1, 100)

        if color < 70:
            if random() < 0.3:
                return Monster(1, [color], 'aggressive')
            return Monster(0, [color], 'passive')
        else:
            if random() < 0.7:
                return Monster(1, [color], 'aggressive')
            return Monster(0, [color], 'passive')

    hyps = [BraveHypothesis(),
            WimpyHypothesis(),
            KNearestNeighbors(3),
            KNearestNeighbors(5),
            KNearestNeighbors(7),
            KNearestNeighbors(11),
            KNearestNeighbors(17),
            KNearestNeighbors(23),
            KNearestNeighbors(29),
            KNearestNeighbors(31),
            KNearestNeighbors(37),
            KNearestNeighbors(41),
            KNearestNeighbors(43),
            KNearestNeighbors(47),
            SimpleProbabilityHypothesis(),
            RandoHypothesis(),
            OptimusPerceptron(47),  # mod 47 universe
            OptimusPerceptron(43),  # mod 43 universe
            OptimusPerceptron(41),  # mod 41 universe
            OptimusPerceptron(37),  # mod 37 universe
            OptimusPerceptron(31),  # mod 31 universe
            OptimusPerceptron(29),  # mod 29 universe
            OptimusPerceptron(23),  # mod 23 universe
            OptimusPerceptron(17),  # mod 17 universe
            OptimusPerceptron(11),  # mod 11 universe
            OptimusPerceptron(7),  # mod 7 universe
            OptimusPerceptron(5),  # mod 5 universe
            OptimusPerceptron(3),  # mod 3 universe
            OptimusPerceptron(2), # even universe
            OptimusPerceptron(1), # lonliest number universe, interesting but not a good idea
            ]

    training_window = 100
    decisioner = Decisioner(hyps, training_window=training_window, trace=True)

    maximum_outcome = 0.0
    total_aggressive = 0.0
    total_passive = 0.0

    actual_outcome = 0.0

    guessed_aggressive = 0.0
    guessed_passive = 0.0

    n = 5000

    for i in range(n):
        monster = create_monster()

        if monster._aggressive == 1:
            total_aggressive += 1
        else:
            maximum_outcome += 1
            total_passive += 1

        guess = decisioner.get_guess(monster.color)

        if guess:
            guessed_passive += 1
        else:
            guessed_aggressive += 1

        outcome = monster.action(guess)
        actual_outcome += outcome
        decisioner.update(monster.color, guess, outcome)

    decisioner._trace = False
    print('======================================')
    print('Total aggressives:   ' + str(total_aggressive) + ' (' + str(total_aggressive / n) + ')')
    print('Total passives:      ' + str(total_passive) + ' (' + str(total_passive / n) + ')')
    print('')
    print('Guessed aggressives: ' + str(guessed_aggressive) + ' (' + str(guessed_aggressive / n) + ')')
    print('Guessed passives:    ' + str(guessed_passive) + ' (' + str(guessed_passive / n) + ')')
    print('')

    agg_diff = guessed_aggressive - total_aggressive

    if agg_diff > 0:
        print ('    We incorrectly categorized ' + str(abs(agg_diff)) + ' passives as aggressive (' + str(agg_diff / n) + ')')
    else:
        print ('    We incorrectly categorized ' + str(abs(agg_diff)) + ' aggressives as passive (' + str(agg_diff / n) + ')')

    print('')
    print('')

    print('Total categorized correctly: ' + str(n - abs(agg_diff)) + ' (' + str((n - abs(agg_diff)) / n) + ')' )
    print('Final hypothesis fitness:    ' + str(decisioner.fitness()))
    print('')
    print('maximum outcome value: ' + str(maximum_outcome) + ' (' + str(maximum_outcome / n) + ')')
    print('actual outcome value:  ' + str(actual_outcome) + ' (' + str(actual_outcome / n) + ')')
    print('outcome ratio:         ' + str(actual_outcome / maximum_outcome))
    print('')
    print('SCORE: ' + str(actual_outcome))
