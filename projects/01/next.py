from enhance42 import *

# returns the next number
# for e.g:
# for number 5  --> returns 6
# for number 42 --> returns 43


def e42_next(number):
    result = e42_add(number, 1)
    return result


# Calling the function
next_number = e42_next(5)
e42_show(next_number)

age = 42
next_year = e42_next(age)
e42_show(next_year)

# Did you understand, how a new function is created.
# If you any doubts write it down otherwise write YES
# and commit this file.
#
