"""
Exercise 03

Write a Python script giving a number between 1 - 10,000 randomly and summarize the total value of the result.
"""

from random import randint

sum = 0

random = randint(1, 10000)
print "the randomized number is", random
while random:
	sum += random % 10
	random /= 10
	
print sum