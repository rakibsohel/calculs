#!/usr/bin/python3

def factorielle(nbe):
	iteration = 1
	nbeIter   = nbe
	while iteration != nbeIter:
		nbe = nbe * iteration
		iteration = iteration + 1
	return(nbe)

def testFctFactorielle():
    if(factorielle(5) == 120):
        return(True)
    else:
        return(False)

def main():
    if(testFctFactorielle() == True):
        print("Test de la fonction factorielle -> OK")
    else:
        print("Test de la fonction factorielle -> NOK")

if __name__ == '__main__':
    main()
