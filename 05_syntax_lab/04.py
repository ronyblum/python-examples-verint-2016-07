"""
Exercise 04

Write a Python script reading user input until user enters blank line. When blank line is entered, print all the inputs from the end to the beginning
"""

#from random import randint

text = []
sent = None

while True:
	sent = raw_input('Enter a Sentence (When done, press enter): ')
	text.append(sent)
	if len(sent) <1: break
text.reverse();
print 'Here is the text inserted:'
for sentence in text:
	print sentence
