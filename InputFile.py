##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : InputFile.py                               ##
## Desc        : This program opens a file based off of the ##
##               users input, then prints out all the       ##
##               variables in a for loop, then closes file  ##
##               It also test if x == to "line 3", and if   ##
##               true, it'll stop printing.                 ##
##                                                          ##
##**********************************************************##

fileName = input("Enter your file name: ")  #Ask user for the name of the file

inputfile = open(fileName ,  "r")           #Opens file that user has input

for x in inputfile:                         #For loop that prints out all

    if x[0:len(x)-1] == "line 3":           #Test of x == "line 3", and will break if true
        break
    print(x)
inputfile.close()                           #Closes file

