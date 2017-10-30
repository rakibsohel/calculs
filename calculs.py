#!/usr/bin/python3

import os

def factorielle(nbe):
	iteration = 1
	nbeIter   = nbe
	while iteration != nbeIter:
		nbe = nbe * iteration
		iteration = iteration + 1
	return(nbe)

def testFctFactorielle():

    bTst    = True
    lst_val = []

    lst_val = lireFicTest("testFactorielle.txt")

    for val in lst_val:
        
        nbeResult = val.strip().split(";")

        if(factorielle(int(nbeResult[0])) != int(nbeResult[1])):
            bTst = False
            
    return(bTst)

def lireFicTest(nomFic):

    lst_File = []
    pathFic = os.getcwd()+"\\"+nomFic
    
    if(os.path.isfile(pathFic) == True):
        print("\nExistence du fichier -> "+nomFic+" : OK")
        try:
            File = open(pathFic,"r")
            lst_File = File.readlines()            
        except:
            print("\nOuverture du fichier de test -> "+nomFic+" : NOK")
    else:
        print("\nExistence du fichier -> "+nomFic+" : NOK")

    return(lst_File)

def main():
    
    if(testFctFactorielle() == True):
        print("\nTest de la fonction factorielle -> OK")
    else:
        print("\nTest de la fonction factorielle -> NOK")

if __name__ == '__main__':
    main()
