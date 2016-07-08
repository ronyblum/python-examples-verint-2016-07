"""
Exercise 05

Write a Python program randomizing an integer number between 1 and 1 million until it's divisible by 7, 13 and 15

"""

from random import randint

while True:
	rand = randint(1, 1000000)
	if rand % 7 == 0 and rand % 13==0 and rand % 15==0: break

print rand