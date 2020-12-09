##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : Program1.py                                ##
## Desc        : This program takes user input for length   ##
##               and width, prints out what the input was,  ##
##               then finds the area and perimeter and      ##
##               prints it out.                             ##
##                                                          ##
##**********************************************************##

length = 0               #A variable for length
width  = 0               #A variable for width
area   = 0               #A variable for area
perim  = 0               #A variable for perimeter

#Enter in all data for length and width
length = float (input("Enter a value for length: "))
width  = float (input("Enter a value for width: "))

#Calculation for area and perimeter
area   = (length * width)
perim  = (length + width ) * 2

#Prints based off of user input
print ("\nYou entered " + str(length) + "cm for the value of length")
print ("You entered "   + str(width) + "cm for the value of width")

#Print out the area
print ("\nThe area is: " + str(area) + " cm")
print ("the perimeter is: " + str(perim) + " cm") 
