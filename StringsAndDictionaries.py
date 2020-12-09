##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : StringsAndDictionaries.py                  ##
## Desc        : This program will take in letters from the ##
##               user, and save it to a dictionary, then put##
##               the number of the same chars that are there##
##               into a dictionary.                         ##
##                                                          ##
##**********************************************************##
userInput = input("Enter some text: ")              #Asks user to input text and saves it in userInput var
myDictionary  = {                                   #Creates a dictionary
    "User Input": userInput                         #Puts the word into the dictonary
    }
for y in userInput:                                 #For loop to go through the letters in the word input
    myDictionary [y] = myDictionary.get(y,0) + 1    #Saves each letter in the dictionary with the number of times the letter comes up

print(myDictionary)                                 #Prints the dictonary
