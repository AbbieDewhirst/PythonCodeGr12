##**********************************************************##
##                                                          ##
## Name        : Abbie Dyck                                 ##
## S/N         : 36800668                                   ##
## Progam Name : ToughListProblem.py                        ##
## Desc        : This program will add the number in the    ##
##               list except for 5, and every number after  ##
##               until the next 3. It then prints the sum,  ##
##               and the values in the list.                ##
##                                                          ##
##**********************************************************##
nums    = [1,2,5,2,4,3,1,1]     #List that will hold all the numbers
numslen = len(nums)             #Variable to hold the number length
isDone  = False                 #Bool to test if the number is 5 or 3
sum     = 0                     #Variable to hold the sum of the numbers
        


for x in nums:                  #For loop to add the numbers
    if x == 5:                  #If x is equal to five, make isDone True
        isDone = True   
    if x == 3 & isDone == True: #If x is equal to 3 and isDone is True, Make isDone Flase and continue adding
        isDone = False
    if isDone == False:         #If isDone is False, keep adding
        sum += x
    else :                      #Else, add 0
        sum += 0
        
print(sum)                      #Prints out the sum
print(nums[0:numslen])          #Prints out the list
