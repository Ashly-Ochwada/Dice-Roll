import random
#range of the dice values 
min_val = 1
max_val = 6

#loop the rolling through user input
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
     #2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again. Any input other than yes or y will stop the loop
    roll_again = input("Roll the Dices Again?") 