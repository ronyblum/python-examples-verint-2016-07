"""
Exercise 02

- Random number between 1-100 + Boom if /7 = 0
"""

from random import randint

sum = 0

for i in range (0,7):
	i = randint(1, 100)
	print i
if i %7 == 0:
	print 'Boom'
