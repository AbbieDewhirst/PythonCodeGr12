##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : TheBiggerBadderBoggleBrainTeaser.py        ##
## Desc        : This program prints out a boggle board, and##
##               ask the user to input all the words they   ##
##               find in the board, the it sees if the words##
##               are in the board or not and prints out the ##
##               final score.                               ##
##                                                          ##
##**********************************************************##
import random                                                           #Imports random

def generateBoard():                                                    #Function to create the boggle board
    for r in range(0,4):                                                #For the range(0,4)
        letter.append([])                                               #Append nothing
        for c in range(0,4):                                            #For the range(0,4)
            letter[r].append(chr(random.randint(65,90)))                #Append a random letter

def printBoard(boggleBoard):                                            #Function to print the boggle board
    for row in boggleBoard:                                             #For the row in boggleBoard
        for col in row:                                                 #For the col in row
            print(col,end = " ")                                        #Print col and a space
        print()                                                         #Prints a blank line

def isWord(wordToSearch):                                               #Function to check if the word is in the boggleBoard
    for x in userGuesses:                                               #For x in the users guesses
        if wordToSearch == x and wordToSearch not in rightWord:         #Check if the word is equal to x and if the word hasn't already been asked
            rightWord.append(wordToSearch)                              #If true appent to the right word list
            return True                                                 #Return true
    return False                                                        #Return false

def guesses():                                                          #Function to ask the user for guesses
    userGuesses = []                                                    #Empty list for the guesses 
    pInput      = input("Enter a word in the grid: ")                   #Ask the user for a word
    while pInput != "#":                                                #If the word is not "#"
        if pInput not in userGuesses:                                   #If the word hasn't already been guessed
            userGuesses.append(pInput)                                  #Append it to the list
        pInput = input("Enter a word in the grid: ")                    #Ask the user for a word
    return(userGuesses)                                                 #Returns the list

def findWord(boggleBoard):                                              #Find word function
    visited = []                                                        #Creates a empty visited list
    string  = ""                                                        #Creates a empty string variable
    for row in range(0,4):                                              #For row in range(0,4)
        visited.append([])                                              #Append nothing
        for col in range(0,4):                                          #for col in range(0,4)
            visited[row].append(0)                                      #Append 0 to visited
   
    for x in range(0,4):                                                #For x in range(0,4)
        for y in range(0,4):                                            #For y in range(0,4)
            findWordsUtil(boggleBoard,visited,x,y,string)               #Calls findWordsUtil

def findWordsUtil(boggleBoard,visited,row,column,string):               #FindWordsUtil function
    visited[row][column] = 1                                            #Makes visitedlist [row][col] equal to 1
    string = string + boggleBoard[row][column]                          #Makes string euqal to string + boggleBoard[row][col]
    if isWord(string):                                                  #If isWord(string) is true
        print(string,"is in the grid")                                  #Print that the word is in the grid
    
    for x in range(row - 1,row + 2):                                    #For x in range(row - 1, row + 2)
        for y in range(column - 1,column + 2):                          #For y in range(col - 1, col + 2)
            if y > -1 and x > -1 and y < 4 and x < 4 and visited[x][y] == 0:#If y and x > -1 and y and x are <4 and visited[x][y] == 0
                findWordsUtil(boggleBoard, visited, x, y, string)       #Calls findWordsUtil
    
    string = string[:len(string)-1]                                     #String = string[:len(string)-1]
    visited[row][column] = 0                                            #visited[row][col] = 0





letter      = []                                                        #Empty list called letter
rightWord   = []                                                        #Empty list called rightWord
score       = 0                                                         #Score = 0

print("~BOGGLE~")                                                       #Print boggle title
generateBoard()                                                         #Calls generateBoard function
printBoard(letter)                                                      #Calls print board function
userGuesses = guesses()                                                 #Calls findWord function
findWord(letter)

for x in rightWord:                                                     #For x in rightWord
    score = score + len(x)                                              #Add the length to score
print("Your total score is:",score)                                     #Print total score
