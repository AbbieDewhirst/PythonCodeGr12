##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : HarderStringAssignment.py                  ##
## Desc        : This program will print out the word in the##
##               variable inString the amount of times the  ##
##               variable n has in it, and appends them all ##
##                                                          ##
##**********************************************************##
inString        = "Hello00"                       ##Var inString to hold the word
n               = 5                               ##Var to hold the amount of times that the word will print
resultString    = ""                              ##Var to hold the complete word

for x in range(n):                                ##For loop to print out the word "n" amount of times
    resultString = resultString + inString[0:4]   ##Takes only the first 4 chars
print (resultString)                              ##Prints out the word
