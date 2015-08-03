"""Decisioner module defines the Decisioner class and the main
method for running the decision framework
"""
from src.hypothesis.Hypothesis import Hypothesis

def get_monsters():
    """Retrieves an iterator of monsters

    :return: Iterator
    :yield: 2-tuple representing the vector
    data of the associated monster
    """
    get_next_monster = lambda: None # Get the monster

    monster = get_next_monster()
    while monster:
        yield monster
        monster = get_next_monster()

def act_on_monster(monster, should_attack):
    """On the given monster, perform an attack if
    the second variable is true

    :param monster: Representing the monster
    :param should_attack: Representing if an attack
    should be made against the monster

    :return: int representing the outcome of the operation
    on the monster. Representing -1, 0, or 1 for the loss,
    neutral and gain outcomes
    """
    outcome = None # perform action should attack on last monster
    return outcome

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
        self._n = 0
        self._trace = trace

    def println(self, msg):
        if(self._trace):
            print(msg)

    def fitness(self):
        return self.get_best_fit_hypothesis.fitness()

    def get_best_fit_hypothesis(self):
        """Gets the hypothesis that is the best fit

        :return: Hypothesis class
        """
        hyp = sorted(self.all_hypothesis, key=lambda h: h.fitness(), reverse=True)
        self.println("All fitnesses in expected order and by class")
        for h in hyp:
            self.println(type(h).__name__ +  ' = ' + str(h.fitness()))
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
        if self._n < self._window:
            return True
        best_hypothesis = self.get_best_fit_hypothesis()
        guess = best_hypothesis.get_guess(vector)

        self.println("Best fit hypothesis: " + str(type(best_hypothesis).__name__))
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
        self._n += 1
