##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : PerfectNumber.py                           ##
## Desc        : This program will print if the number being##
##               tested is a perfect number or not.         ##
##                                                          ##
##**********************************************************##
def is_perfect(number):         #Function called is_perfect
    add = 0                     #Variable to hold sum
    for i in range(1,number):   #For loop to add the numbers
        if number % i == 0:     #For loop to check if remainder is equal to 0
            add = add + i       #Variable plus var + i  
    if (add == number):         #If ass is equal to number
        print("True")           #Print true (Because number is true)
    else:                       #Else
        print("False")          #Print False (Because number is false)
            
is_perfect(12)                  #Runs function
