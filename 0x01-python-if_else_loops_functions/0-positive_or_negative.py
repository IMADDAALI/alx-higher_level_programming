#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number:f} is positive")
elif number == 0:
    print(f"{number:f} is zero")
else:
    print(f"{number:f} is negative")

