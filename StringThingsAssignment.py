##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : StringThingsAssignment.py                  ##
## Desc        : This program will print out the word in the##
##               variable myString the amount of times the  ##
##               variable myNumber has in it.               ##
##                                                          ##
##**********************************************************##
myString    = "potatoe "                    ##Var myString to hold the word
myNumber    = 5                             ##Var to hold the amount of times that the word will print
myNewString = ""                            ##Var to hold the complete word

for x in range(myNumber):                   ##For loop to print out the word
    myNewString = myNewString + myString    ##Appends the words

print (myNewString)                         ##Prints the word
