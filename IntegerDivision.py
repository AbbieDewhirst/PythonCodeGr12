##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : IntegerDivision.py                         ##
## Desc        : This program takes a list, takes out 1 of  ##
##               the dups from the lowest and highest nums, ##
##               and prints the numSum//listRange.          ##
##                                                          ##
##**********************************************************##

balancedList = [1,1,2,3,4,1,4,9,9,9,9]                                                  #list to find sum of
maxNum = max(balancedList)                                                              #Finds the max number in the list
maxNumInd = balancedList.index(maxNum)                                                  #Finds the max numbers ele number
minNum = min(balancedList)                                                              #Finds the min number in the list
minNumInd = balancedList.index(minNum)                                                  #Finds the min number ele number

listLen = len(balancedList)                                                             #Finds the length of the list
numSum = sum(balancedList)                                                              #Finds the sum of the list

if maxNumInd == listLen - 1:                                                            #If the maxNumInd is the last number
    if maxNum == balancedList[maxNumInd - 1]:                                           #Only test for the number to the left
        balancedList.pop(maxNumInd)                                                     #Delete the max number because there are more than 1 of the same 
else:
    if maxNum == balancedList[maxNumInd + 1] or maxNum == balancedList[maxNumInd - 1]:  #If the max number is the same as any of the numbers next to it
        balancedList.pop(maxNumInd)                                                     #Delete the max number because there are more than 1 of the same
    if minNum == balancedList[minNumInd + 1] or minNum == balancedList[minNumInd - 1]:  #If the min number is the same as any of the numbers next to it
        balancedList.pop(minNumInd)                                                     #Delete the min number because there are more than 1 of the same

print(numSum//listLen)                                                                  #Prints the remainder of the number sum and the list length
