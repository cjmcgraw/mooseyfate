"""Decisioner module defines the Decisioner class and the main
method for running the decision framework
"""

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

class Decisioner:
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

    def __init__(self, hypothesis):
        """Initializes the Decisioner """
        self.all_hypothesis = hypothesis

    def get_best_fit_hypothesis(self):
        """Gets the hypothesis that is the best fit

        :return: Hypothesis class
        """
        return max(self.all_hypothesis, key=lambda h: h.fitness())

    def should_attack(self, vector):
        """Retrieves a boolean value representing if the given
        monster should be attacked

        :param vector: 2-tuple representing the monster to
        be decided on

        :return: bool
        """
        best_hypothesis = self.get_best_fit_hypothesis()
        return best_hypothesis.get_guess(vector)

    def learn(self, vector, attacked, outcome):
        """Applies the given monster-vector and outcome
        to the hypothesis

        :param vector: 2-tuple representing the monster-vector

        :param attacked: bool representing if the monster-vector
        was attacked

        :param outcome: int representing if the outcome of
        acting on the vector
        """
        for hypothesis in self.all_hypothesis:
            hypothesis.update(vector, attacked, outcome)

if __name__ == "__main__":
    from hypothesis.WimpyHypothesis import WimpyHypothesis
    from hypothesis.BraveHypothesis import BraveHypothesis

    from lib.TestingEnvironment import monster_generator

    brave = BraveHypothesis()
    wimpy = WimpyHypothesis()

    decisioner = Decisioner([brave, wimpy])

    genny = monster_generator()
    monsters = [next(genny) for x in range(100)]

    for monster in monsters:
        should_attack = decisioner.should_attack(monster)
        outcome = act_on_monster(monster, should_attack)
        decisioner.learn(monster, should_attack, outcome)

    print(vars(decisioner))
    print('')
    print('Brave hypothesis: ' + str(vars(decisioner.all_hypothesis[0])))
    print('')
    print('Wimpy hypothesis: ' + str(vars(decisioner.all_hypothesis[1])))
