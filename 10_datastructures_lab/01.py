"""
Exercise 1

Write a Python program that prints the IP addresses of the computers in the list. If one of the name doesn't appear in the file, return error message
"""

import sys

hosts={}

hostnames = set(sys.argv[1:])

with open('hosts.txt', 'r') as f:
	for line in f:
		(hostname,ipaddress) = line.strip('\n').split('=')
		hosts[hostname]=ipaddress


for name in hostnames:
	if name in hosts:
		print "The IP requested of %s is %s" % (name, hosts[name])
	else:
		print "%s doesn't exist in the hosts file" % (name)

f.close()