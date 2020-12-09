##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : Assignment1.py                             ##
## Desc        : This program test diffrent variables       ##
##               and their values and type, and prints them ##
##               out based off of the results.              ##
##                                                          ##
##**********************************************************##

#Creates varibles
mystring = "hello"                                          #String variable that holds "hello"
myfloat = 10.0                                              #Float variable that holds 10.0
myint = 20                                                  #Integer variable that holds 20

#If statements to test variables and print
if mystring == "Hello" and isinstance(mystring, str):       #Test if the string is "Hello
    print ("Your string contains " + mystring)              #Prints if test is true

if myfloat == 20.0 and isinstance(myfloat, float):          #Test if the float is 20.0
    print ("My float conatins " + str(myfloat))             #Prints if the test is true

if myint == 43 and isinstance(myint, int):                  #Test if the integer is 43
    print ("The Integer Variable contains " + str(myint))   #Prints if the test is true

