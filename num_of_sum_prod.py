#!/usr/bin/python

if __name__ == "__main__":
	seed  = int(raw_input("Enter a number to calculate result:"))
	operation = raw_input("Enter an operation to perform:")

	result = 1

	for i in range(result,seed):
		if operation == '*':
			result*= i
		elif operation == '+':
			result+= i

	print "Final result %s" %result
		
