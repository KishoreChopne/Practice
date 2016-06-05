#!/usr/bin/python

if __name__ == "__main__":
	seed  = int(raw_input("Enter a number to calculate sum ?:"))

	sum = 0

	for i in range(seed):
		sum += i

	print "Final sum %s" %sum
		
