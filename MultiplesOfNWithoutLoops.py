##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : MultiplesOfNWithoutLoops.py                ##
## Desc        : This program will print out the multiples  ##
##               of m, and it will print out the first n    ##
##               numbers.                                   ##
##                                                          ##
##**********************************************************##
def multiple(m, n):                 #Creates a function
    a = range(n, (m * n)+1, n)      #Makes a equal to the range of n - ((m*n)+1) so it will know how many numbers to print out
      
    print(*a)                       #Prints out all of the multiples of m
  
m = int(input("Enter m number: "))  #Variable m
n = int(input("Enter n number: "))  #Variable n
multiple(m, n)                      #Runs the function
