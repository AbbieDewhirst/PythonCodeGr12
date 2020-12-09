##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : RegEx.py                                   ##
## Desc        : This program is a test of regex and will   ##
##               a bunch of diffrent regex metachars.       ##
##                                                          ##
##**********************************************************##
import re                                       #Imports regex features

def printFun(x):                                #A function I use to print if its a match or not
    if x:                                       #If x is true
        print("MATCH")                          #Print that it was a match
    else:                                       #Else
        print("NO MATCH")                       #Print no match

inData = "The rain in Spain falllz mainly in the plane but not down_the drain, I am not to blame."  #Variable inData that holds the string we are testing

printFun(re.search("^The drain$", inData))      #Test to see if inData starts with "The" and ends with "drain":

printFun(re.search('aib*', inData))             #Searches for a string “ai” that is  followed by zero or more b's

printFun(re.search("to b+", inData))             #Test to see if inData has the string “to“ that has an a followed by one or more b's 

printFun(re.search("al+", inData))              #Test to see if inData has an ‘a’ followed by one or more l's

print(re.findall("[a-z]+_[a-z]+", inData))      #Finds all lowercase letters joined with a underscore

printFun(re.search("b.*e$", inData))            #Test to see if inData has an 'b' followed by anything, ending in 'e'

printFun(re.search("\w*z.\w", inData))          #Test to see if inData matches a word containing 'z'

print(re.sub("\.|\_|\s|,", ":", inData))        #Subs any space, comma or dot with a colon

print(re.sub(r"a|,|\.", "@", inData,2))         #Replaces max 2 occurrences of 'a', a comma or dot with a @

print(re.findall(r"\b\w{4,}\b", inData))        #Finds all words that are at least 4 characters long
