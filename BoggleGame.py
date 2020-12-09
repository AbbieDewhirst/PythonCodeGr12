import random

def generateBoard():
    for r in range(0,4):
        letter.append([])
        for c in range(0,4):
            letter[r].append(chr(random.randint(65,90)))

def printBoard(boggleBoard):
    for r in boggleBoard:
        for c in r:
            print(c,end = " ")
        print()

def guesses():
    userGuesses = [] 
    playerInput   = input("Enter a word in the grid: ")
    while playerInput != "#":
        if playerInput not in userGuesses:
            userGuesses.append(playerInput)
        playerInput = input("Enter a word in the grid: ")

    return(userGuesses)

def findWord(boggleBoard):
    visited       = []
    currentWord   = ""

    for r in range(0,4):
        visited.append([])
        for c in range(0,4):
            visited[r].append(0)
   
    for x in range(0,4):
        for y in range(0,4):
            findWordsUtil(boggleBoard,visited,x,y,currentWord)

def findWordsUtil(boggleBoard,visited,row,column,currentWord):
    visited[row][column] = 1
    currentWord = currentWord + boggleBoard[row][column] 
    if isWord(currentWord):
        print(currentWord,"is in the grid") 
    
    for x in range(row-1,row+2):
        for y in range(column-1,column+2):
            if x >-1 and y >-1 and x<4 and y <4 and visited[x][y] == 0:
                findWordsUtil(boggleBoard,visited,x,y,currentWord)
    
    currentWord = currentWord[:len(currentWord)-1]

    visited[row][column] = 0 

def isWord(wordToSearch):
    
    for x in userGuesses:
        
        if wordToSearch == x and wordToSearch not in rightWord:
            rightWord.append(wordToSearch)
            return True
        
    return False

letter = []
rightWord = []
total = 0 

print("~BOGGLE~")
generateBoard() 
printBoard(letter)
userGuesses = guesses()
findWord(letter)

for x in rightWord:
    total = total + len(x)
print("Your total score is:",total)


            
        
    
