# Give the implementation of e42_double
# Need to implement e42_triple

from enhance42 import *


def e42_negative(number):
    result = e42_substract(0, number)
    return result


def e43_increment(number):
    result = e42_add(number, 1)
    return result


def e43_decrement(number):
    result = e42_substract(number, 1)
    return result


def e42_double(number):
    result = e42_add(number, number)
    return result


def e42_triple(number):
    result = e42_double(number)
    result = e42_add(number, result)
    return result


neg_of_5 = e42_negative(5)
e42_show(neg_of_5)

increment_of_5 = e42_increment(5)
e42_show(increment_of_5)

decrement_of_5 = e42_decrement(5)
e42_show(decrement_of_5)


double_of_5 = e42_double(5)
e42_show(double_of_5)

triple_of_5 = e42_triple(5)
e42_show(triple_of_5)
