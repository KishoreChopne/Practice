#!/usr/bin/python

def badfoo(lst=[]):
	lst.append(1)
	print lst

def goodfoo(lst=None):
	if lst is None:
		lst = []
	lst.append(1)
	print lst

if __name__ == '__main__':
	badfoo()
	badfoo()
	badfoo()
	goodfoo()
	goodfoo()
	goodfoo()
