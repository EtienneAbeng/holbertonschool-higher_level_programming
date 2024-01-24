#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#Check if the number is positive
if (number > 0):
    print(f"{number} is positive")
#Check if the number is zero
elif (number == 0):
    print(f"{number} is zero")
#Check if the number is negative
else:
    print(f"{number} is negative")
