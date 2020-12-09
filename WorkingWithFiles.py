##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : WorkingWithFiles.py                        ##
## Desc        : This program test to see if a file exsist. ##
##               If it does, it'll delete the file, then    ##
##               create it. It then takes in 3 city names,  ##
##               and 1 country name. It then prints this all##
##               out to the screen.                         ##
##                                                          ##
##**********************************************************##
import os                                               #Imports the os
#Step One
fileName = input("Enter your file name: ")              #Ask user for the name of the file

if os.path.exists(fileName):                            #Checks to see if the file exsist
  os.remove(fileName)                                   #Deletes the File if it exsist

dataFile = open(fileName, "w")                          #Then creates the file

#Step Two
cityName = input("Enter the name of a city: ")          #Ask user for a city name
dataFile.write(cityName + "\n")                         #Writes the city name to the file

cityName = input("Enter the name of a city: ")          #Ask user for a city name
dataFile.write(cityName + "\n")                         #Writes the city name to the file

cityName = input("Enter the name of a city: ")          #Ask user for a city name
dataFile.write(cityName + "\n")                         #Writes the city name to the file

dataFile.close()                                        #Closes the file

#Step Three

dataFile = open(fileName, "a")                          #Opens the file

countryName = input("Enter the name of a country: ")    #Ask for a country name
dataFile.write(countryName + "\n")                      #Writes the country name to the file

dataFile.close()                                        #Closes the file

#Step Four

dataFile = open(fileName, "r")                          #Opens the file

print (dataFile.read())                                 #Prints out all of the data

dataFile.close()                                        #Closes the file


