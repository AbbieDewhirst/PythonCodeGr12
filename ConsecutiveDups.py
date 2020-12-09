##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : ConsecutiveDups.py                         ##
## Desc        : This program will remove the dupes from a  ##
##               list that was created by the tuple, and    ##
##               prints out the result.                     ##
##                                                          ##
##**********************************************************##
aTuple = (1,3,5,8,7,2,1,5,5,5,8,7,4,4,4)    #Creates a tuple
aList = list(aTuple)                        #Creates a list from the tuple
x = 0                                       #Zeros out var x

while x < len(aList)-1:                     #While loop to test if there are any consecutive duplicates
    if aList[x] == aList[x+1]:              #Checks to see if they are the same
        del aList[x]                        #Delete if they are the same
    else:
        x = x+1                             #If they aren't the same move on to next var

print(aList)                                #Prints out the list

newList = list(dict.fromkeys(aList))        #Creates a new list based off of the previous one created with no consecutive dupes, and deletes all dupes

print(newList)                              #Prints out the new list

