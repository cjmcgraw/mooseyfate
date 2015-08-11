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

    k_n_one = 0
    k_zero = 0
    k_one = 0

    n = 5000

    for i in range(n):
        monster = create_monster()

        if monster._aggressive == 1:
            total_aggressive += 1
        else:
            maximum_outcome += 1
            total_passive += 1

        guess = decisioner.get_guess(monster.color)

        if not guess:
            guessed_passive += 1
        else:
            guessed_aggressive += 1

        outcome = monster.action(guess)
        actual_outcome += outcome
        if (outcome == 0):
            k_zero += 1
        if (outcome == 1):
            k_one += 1
        if (outcome == -1):
            k_n_one += 1
        decisioner.update(monster.color, guess, outcome)
        print ('@Guess:'+str(guess)+' outcome:'+str(outcome))
        print ('@cumulative :'+str(k_zero+k_one+k_n_one))
        print ('      : k(Zeros)= '+str(k_zero))
        print ('      : k(Ones)= '+str(k_one))
        print ('      : k(NegOne)= '+str(k_n_one))

    decisioner._trace = False

    agg_diff = guessed_aggressive - total_aggressive
    passive_diff = guessed_passive - total_passive

    print('====================================== Mike Analysis =============')
    print ('@analysis for cardinality :'+str(k_zero+k_one+k_n_one))
    print ('      : k(Zeros)= '+str(k_zero))
    print ('      : k(Ones)= '+str(k_one))
    print ('      : k(NegOne)= '+str(k_n_one))
    print ('score hits on this many monsters : ' + str(k_one-k_n_one) + 'AND dodged this many monsters: ' + str(k_zero))
    print('Total aggressives:   ' + str(total_aggressive) + ' (% of total : ' + str(total_aggressive / n) + ')')
    misclass_aggro = abs(agg_diff)/total_aggressive
    print(' misclassified aggressives: abs(guessed aggro - total aggro) / total aggro =' + str(misclass_aggro))
    print(' positively classified aggressives: 1- (abs(guessed aggro - total aggro) / total aggro) =' + str(1-misclass_aggro))
    misclass_passive = abs(passive_diff)/total_passive
    print('Total passives:      ' + str(total_passive) + ' (% of total : ' + str(total_passive / n) + ')')
    print(' misclassified passives: abs(guessed passive - total passive) / total passive =' + str(misclass_passive))
    print(' positively classified passives: 1-(abs(guessed passive - total passive) / total passive) =' + str(1-misclass_passive))
    success_mean = float(abs(1-misclass_aggro) + abs(1-misclass_passive)) /2.0
    print('score                                     : ' + str(k_one-k_n_one))
    print('max potential score (assume no aggressive): ' + str(k_one))
    print('success ratio: score/max score = ' + str(float(k_one-k_n_one)/float(total_passive)) )
    print('successful classification mean: (classified aggressives + classified passives)/2 = ' + str(success_mean))

    print('====================================== Carl Analysis =============')
    print('Total aggressives:   ' + str(total_aggressive) + ' (' + str(total_aggressive / n) + ')')
    print('Total passives:      ' + str(total_passive) + ' (' + str(total_passive / n) + ')')
    print('')
    print('Guessed aggressives: ' + str(guessed_aggressive) + ' (' + str(guessed_aggressive / n) + ')')
    print('Guessed passives:    ' + str(guessed_passive) + ' (' + str(guessed_passive / n) + ')')
    print('')
    print('guessed aggro - total aggro = ' + str(agg_diff) + ' missed points')
    print('guessed_passive - total passive = ' + str(passive_diff) + ' miscategorized passive')
    print('Total passive - Agressives we lost points to('+str(agg_diff)+') = Score:' + str(total_passive - agg_diff))
    print('')




    if agg_diff > 0:
        print ('    We incorrectly categorized ' + str(abs(agg_diff)) + ' passives as aggressive (' + str(agg_diff / n) + ')')
    else:
        print ('    We incorrectly categorized ' + str(abs(agg_diff)) + ' aggressives as passive (' + str(agg_diff / n) + ')')
    print ('    Theoretical Score = Total Passives(aka. max-score) - Miscategorized Aggro that cost us points = ' + str(total_passive - abs(agg_diff)) )
    print ('    Theoretical Ratio = Theoretical Score / Total Passives(aka. max-score) =' +  str((total_passive - abs(agg_diff))/total_passive)  )
    print('')
    print('')

    print('Total categorized correctly: ' + str(n - abs(agg_diff)) + ' (' + str((n - abs(agg_diff)) / n) + ')' )
    print('Final hypothesis fitness:    ' + str(decisioner.fitness()))
    print('')
    print('ratio of total passive to number monsters : ' + str(total_passive/n) )
    print('maximum outcome value: ' + str(maximum_outcome) + ' (' + str(maximum_outcome / n) + ')')
    print('actual outcome value:  ' + str(actual_outcome) + ' (' + str(actual_outcome / n) + ')')
    print('outcome ratio:         ' + str(actual_outcome / maximum_outcome))
    print('')
    print('SCORE: ' + str(actual_outcome))
