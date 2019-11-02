#!/usr/bin/env python3

import operator
import readline
from retrying import retry

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': pow
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

@retry(stop_max_attempt_number=10)
def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print("Result: ", result)
        except Exception as e:
            print(e)
            print("Please try again.")
            raise

if __name__ == '__main__':
    main()
