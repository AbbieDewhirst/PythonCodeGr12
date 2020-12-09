##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : TacoCatLevel4FSEAD.py                      ##
## Desc        : This program will read in a bunch of words ##
##               from a file, and will test if each is a    ##
##               palindrome, and will print out a mini      ##
##               report with the results of each word.      ##
##                                                          ##
##**********************************************************##
def palindrome(string):                             #Palindrome function with input string
    if len(string) < 2:                             #If the len of string is less than 2
        return True                                 #Return true
    else:                                           #else
        if string[0] == string[-1]:                 #If string[0] is equal to string[-1]
            return palindrome(string[1:-1])         #Return palindrome(string[1:-1])
        else:                                       #Return false
            return False
        
inputFile = open("e:\\tacocat.txt","r")             #Opens the file

num = inputFile.readline()                          #Num equal to first line in the file
string = inputFile.readline()                       #String equal to next line in file
newList = []                                        #Makes newList a list

for i in string[0]:                                 #For i in string[0]
    newList.append(string.split(","))               #Append the split word at the "," to the newList

for x in range(int(num)):                           #For x in the range of num

    if palindrome(newList[0][x])== True:            #If the Palindrome function returns true
        print("THE TACOCAT TEST")                   #Print title
        print("================")                   #Prints lines so it'll look good
        print("Word being checked:", newList[0][x]) #Prints the word being checked
        print("…Testing…")                          #Prints testing
        print("Test Result:", newList[0][x], "\n")  #Prints the test result
    else:
        print("THE TACOCAT TEST")                   #Print title
        print("================")                   #Prints lines so it'll look good
        print("Word being Checked:", newList[0][x]) #Prints the word being checked
        print("…Testing…")                          #Prints testing
        print("Test Result: !TACOCAT!\n")           #Prints !TACOCAT! which means the word is not a Palindrome

print(newList)                                      #Prints the list out
inputFile.close()                                   #Closes the file
