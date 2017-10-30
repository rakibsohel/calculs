#!/usr/bin/python3

def factorielle(nbe):
	iteration = 1
	nbeIter   = nbe
	while iteration != nbeIter:
		nbe = nbe * iteration
		iteration = iteration + 1
	print(nbe)

def main():
    factorielle(5)

if __name__ == '__main__':
    main()
