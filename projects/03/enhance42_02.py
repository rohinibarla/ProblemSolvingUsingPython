# code from previous project

from enhance42 import *


def e42_negative(number):
    result = e42_substract(0, number)
    return result


def en42_product(number1, number2):
    if number1 < 0 and number2 < 0:
        number1 = e42_negative(number1)
        number2 = e42_negative(number2)

    result = 0
    if number1 > 0:
        while number1 > 0:
            result = e42_add(result, number2)
    else:
        while number2 > 0:
            result = e42_add(result, number1)

    return result


def en42_remainder(divident, divisor):
    remainder = divident
    while remainder >= divisor:
        remainder = e42_substract(remainder, divisor)
    return remainder


def en42_questient(divident, divisor):
    questient = 0
    while divident >= divisor:
        divident = e42_substract(divident, divisor)
        questient = e42_increment(questient)
    return questient
