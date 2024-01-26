#!/usr/bin/python3

# Import a function from another file
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":

    a = 10
    b = 5

    # Different function used in file imported
    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)

    # Print the different oepration realized after passage in parameter
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
