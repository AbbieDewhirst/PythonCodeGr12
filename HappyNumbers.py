##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : HappyNumbers.py                            ##
## Desc        : This program will check if the numbers in  ##
##               each list, and add or subtract 1 from the  ##
##               happiness if it finds it in the list (After##
##               reading from a file) and print the final   ##
##               happiness result.                          ##
##                                                          ##
##**********************************************************##
inputfile = open("e:\\input.txt" ,  "r")    #Reads in the file

listEle = inputfile.read(1)                 #Makes the first digit equal to the length of the first digit
temp = inputfile.read(1)                    #Temp value for the space
listAEle = inputfile.read(1)                #Makes the second digit equal to the length of the second digit
listBEle = listAEle                         #Makes the length of listAEle the length of listBEle
temp = inputfile.read(1)                    #Temp value for the space

AList = []                                  #Makes AList a list
listA = []                                  #Makes listA a list
listB = []                                  #Makes listB a list

AList = inputfile.readline().split()        #Makes AList equal to the second line in the file
listA = inputfile.readline().split()        #Makes listA equal to the third line in the file
listB = inputfile.readline().split()        #Makes listB equal to the fourth line in the file

happiness = 0                               #Sets happiness to zero

for x in range(0,int(listEle)):             #For all of the elements in the first list
    for y in range(0, int(listAEle)):       #For all of the elements in the second list
        if AList[x] == listA[y]:            #If the numbers are the same
            happiness = happiness + 1       #Add 1 to happiness
    for z in range(0, int(listBEle)):       #For all of the elements in the third list
        if AList[x] == listB[z]:            #If the numbers are the same
            happiness = happiness - 1       #Subtract 1 from happiness

print(happiness)                            #Print out happiness
