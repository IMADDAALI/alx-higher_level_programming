#!/usr/bin/python3
import random

random_number = random.randint(-10, 10)

if random_number > 0:
    print(f"{random_number:d} is positive")
elif random_number == 0:
    print(f"{random_number:d} is zero")
else:
    print(f"{random_number:d} is negative")

