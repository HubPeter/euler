#!/usr/bin/env python
def count(number):
	sum  = 0
	for i in range(number):
		if i%3==0 or i%5==0: 
			sum +=i
	return sum

if __name__ == '__main__':
	print count(10)
	print count(1000)
