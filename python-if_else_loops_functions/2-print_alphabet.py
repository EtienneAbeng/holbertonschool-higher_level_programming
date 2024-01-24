#!/usr/bin/python3

#Use some numbers in the table ascii (a = 97 & z = 123)
for ascii in range(97, 123):
    #{:c} is a convention in python and 'end'allow to print the same line
    print("{:c}".format(ascii),end ="")
