""" This module represents the testing framework used to
generate potential run scenarios for the framework"""

from random import random, randint

global COLOR_CATEGORY_1
global COLOR_CATEGORY_1_AGGRO
global COLOR_CATEGORY_2
global COLOR_CATEGORY_2_AGGRO

COLOR_CATEGORY_1 = 0.7
COLOR_CATEGORY_1_AGGRO = 0.6
COLOR_CATEGORY_2 = 1 - COLOR_CATEGORY_1
COLOR_CATEGORY_2_AGGRO = 0.05


def aggro_probability():
    p1 = COLOR_CATEGORY_1 * COLOR_CATEGORY_1_AGGRO
    p2 = COLOR_CATEGORY_2 * COLOR_CATEGORY_2_AGGRO
    return p1 + p2

def passive_probability():
    return 1 - aggro_probability()


class Monster(object):
    """Monster class encapsulates the aggressiveness and
    color. The aggressiveness should not be accessed and
    as such its name has been mangled """

    def __init__(self, aggressive, color, label):
        """Initializes the monster"""
        self._aggressive = aggressive
        self.color = color
        self.label = label

    def action(self, should_attack):
        """Act on the monster"""
        if not should_attack:
            return 0
        if self._aggressive:
            return -1
        return 1

def monster_generator():
    """Provides a generator for monsters"""
    while True:
        color = randint(1, 100)
        if (color / 100.0) <= COLOR_CATEGORY_1:
            if random() <= COLOR_CATEGORY_1_AGGRO:
                yield Monster(1, color, 'A')
            else:
                yield Monster(0, color, 'A')
        else:
            if random() <= COLOR_CATEGORY_2_AGGRO:
                yield Monster(1, color, 'B')
            else:
                yield Monster(0, color, 'B')

def run_tests(hypothesis, trials=100):
    generator = monster_generator()

    score = 0.0
    max_score = 0.0

    for x in range(trials):
        monster = next(generator)

        if monster._aggressive == 0:
            max_score += 1

        guess = hypothesis.get_guess(monster)
        outcome = monster.action(True)
        hypothesis.update(monster, guess, outcome)

        score += outcome

    print('Maximum Score: ' + str(max_score))
    print('Score        : ' + str(score))
    print('Success Rate : ' + str(score / max_score))
    print('')
    print('True passive p-value : ' + str(passive_probability()))
