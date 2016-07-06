"""
Exercise 1

- Largest number between 10 numbers
"""


num = []
for i in range(1,11):
	num.append(raw_input('Please enter the %s number: ' % i))
print 'The Largest number entered is: ', max(num)