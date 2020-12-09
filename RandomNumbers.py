##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : RandomNumbers.py                           ##
## Desc        : This program will test if the number the   ##
##               user types in is higher, lower, or equal to##
##               what the random number was, and prints out ##
##               how many guesses it took.                  ##
##                                                          ##
##**********************************************************##
import random                                       #imports the random number generator

def checkNumber(guess, correct):                    #Funtion to test if guess is correct or not
    if guess < correct:                             #If guess is less than the correct number
        print("HIGHER")                             #Print that the number is higher
        return False                                #Return false
    elif guess > correct:                           #If guess is more than the correct number
        print("LOWER")                              #Print that the number is lower
        return False                                #Return false
    else:                                           #Else (The number is correct)
        print("CORRECT")                            #Print correct
        return True                                 #Return true


randomNum = random.randint(1,99)                    #Generates a random int
counter = 1                                         #Sets counter to 1
guess = input("Enter your guess: ")                 #Ask user to enter their guess

while guess != "exit":                              #While guess is not "exit"
    counter += 1                                    #Adds one to the counter
    isFinish = checkNumber(int(guess), randomNum)   #Runs the function
    guess = input("Enter your guess: ")             #Ask user to enter their guess
    if isFinish == True:                            #If isFinish is true
        break                                       #Break out of the while loop

print("You have took " + str(counter) + " gusses")  #Print how many guesses you took
