##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : LabTest.py                                 ##
## Desc        : This program will take in the button the   ##
##               user wants to press and rearrange the list ##
##               depending on the button number and number  ##
##               number of presses.                         ##
##                                                          ##
##**********************************************************##
def playlist_fun(b,n,newplay):                                                          #Defines the function
    if b == 1:                                                                          #If b is one
        for x in range(n):                                                              #For loop to run 'n' times
            newplay = newplay[1] + newplay[2] + newplay[3] + newplay[4] + newplay[0]    #Sort the list for the button 1 pattren
        return(newplay)                                                                 #Return the new playlist
    if b == 2:                                                                          #If b is two
        for x in range(n):                                                              #For loop to run 'n' times
            newplay = newplay[4] + newplay[0] + newplay[1] + newplay[2] + newplay[3]    #Sort the list for the button 2 pattren
        return(newplay)                                                                 #Return the new playlist
    if b == 3:                                                                          #If b is three
        for x in range(n):                                                              #For loop to run 'n' times
            newplay = newplay[1] + newplay[0] + newplay[2] + newplay[3] + newplay[4]    #Sort the list for the button 3 pattren
        return(newplay)                                                                 #Return the new playlist
    if b == 4:                                                                          #If b is four
        return(newplay)                                                                 #Return the last sorted playlist
        
    
placholder = 10000                                                                      #Placeholder var to run the for loop
playlist = ["A","B","C","D","E"]                                                        #Starting playlist
newPlay = playlist                                                                      #newPlay is equal to playlist
for x in range(placholder):                                                             #For loop to run the code as many times as possible
    b = int(input("Button number: "))                                                   #Ask user for 'b' variable
    n = int(input("Number of presses: "))                                               #Asks user for 'n' variable
    if b != 4:                                                                          #If 'b' is not 4
        newPlay = playlist_fun(b,n,newPlay)                                             #Run the function with the newPlay variable
    else:                                                                               #Else ('b' is 4)
        print(playlist_fun(b,n,newPlay))                                                #Print out the final playList
        break                                                                           #And break out of the for loop

