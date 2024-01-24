#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i != 9 or j != 9:
            print("{}{}".format(i, j % 10), end=", ")
        else:
            print("{}{}".format(i, j % 10))
'''
for i in range(0, 100):
    if i < 99:
        print("{:02}".format(i), end=", ")
    else:
        print("{}".format(i))'''
