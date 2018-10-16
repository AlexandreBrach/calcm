# -*- coding: utf-8 -*-
""" Entrainement de calcul mental
"""

from random import randint


class RandomBetween:
    "Return a random number between minimum and maximum"

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def get(self):
        "return the random number"
        return randint(self.minimum, self.maximum)


class FiveMultiple:
    "Always return a 5 multiple"

    def __init__(self, min_fact, max_fact):
        self.min_fact = min_fact
        self.max_fact = max_fact

    def get(self):
        return 5 * randint(self.min_fact, self.max_fact)


class Constant:
    "Always return a 5 multiple"

    def __init__(self, num):
        self.num = num

    def get(self):
        return self.num


class Addition:
    def num_operands(self):
        return 2

    def set_operands(self, operands):
        self.operands = operands

    def result(self):
        return self.operands[0] + self.operands[1]

    def format(self):
        return "{} + {}".format(self.operands[0], self.operands[1])


class Multiplication:
    def num_operands(self):
        return 2

    def set_operands(self, operands):
        self.operands = operands

    def result(self):
        return self.operands[0] * +self.operands[1]

    def format(self):
        return "{} x {}".format(self.operands[0], self.operands[1])


def batch(operation, randomizer1, randomizer2):
    """ Series d'opérations
    """
    op1 = randomizer1.get()
    op2 = randomizer2.get()
    op = operation()
    op.set_operands([op1, op2])
    result = op.result()
    prompt = op.format() + " = "
    user_response = raw_input(prompt)
    if user_response == str(result):
        print "GOOD"
    else:
        print "BAD! It was {}.".format(result)


if __name__ == "__main__":
    for i in range(1, 10):
        batch(Addition, RandomBetween(11, 99), RandomBetween(11, 99))
    for i in range(1, 10):
        batch(Multiplication, RandomBetween(11, 20), RandomBetween(2, 9))
    for i in range(1, 10):
        batch(Multiplication, RandomBetween(100, 999), RandomBetween(2, 3))
    for i in range(1, 10):
        batch(Multiplication, RandomBetween(100, 999), FiveMultiple(1, 1))
    for i in range(1, 10):
        batch(Addition, RandomBetween(1000, 9999), RandomBetween(1000, 9999))
    for i in range(1, 10):
        batch(Multiplication, RandomBetween(19, 99), Constant(11))
    for i in range(1, 10):
        batch(Multiplication, RandomBetween(19, 99), Constant(15))
