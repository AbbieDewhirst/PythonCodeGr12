##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : fibSeq.py                                  ##
## Desc        : This program is the Fibonacci sequence and ##
##               will find the number in the sequence that  ##
##               is asked for and print out the sequence.   ##
##                                                          ##
##**********************************************************##
def fib_seq(n):                             #defines the fib function 
    if n < 2:                               #If n is less than 2
        return n                            #Return n
    else:                                   #Else
        return fib_seq(n-2) + fib_seq(n-1)  #Return the sequence(n-2) + sequence(n-1)
    
print(fib_seq(11))                           #Runs the sequence
