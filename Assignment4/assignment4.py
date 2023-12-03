'''
Daniel Ribuffo - Assignment 4 
CSCE A 101 - FA23
'''

#Any needed import statements

from assignment4classes import ChildName
import random

# Functions to be used:
def choice_checker(girl, boy, choice):
    '''
    This function takes in a boy and girl object, and determines which name was used
    more in 2015 via a comparison of the value objects.birth typecasted as an integer. Then 
    based on which choice you make during the game it will output True or False depending on 
    what player input was chosen.
    '''
    if int(choice) == 1:
        if int(girl.births) > int(boy.births):
            return True
        elif int(girl.births) < int(boy.births):
            return False
    elif int(choice) == 2:
        if int(boy.births) > int(girl.births):
            return True
        elif int(boy.births) < int(girl.births):
            return False

#Opens the two files and gets the list of boynames and girlnames.

bf = open('boynames2015.txt', 'r') 
boy_names_file_list = bf.readlines() 
bf.close() 

gf = open('girlnames2015.txt', 'r') 
girl_names_file_list = gf.readlines() 
gf.close() 

#Creating a list of objects, one for boynames and one for girlnames

boy_names_object_list = []
for line in boy_names_file_list:
    line = line.split()
    rank = line[0]
    name = line[1]
    births = line[2]
    new_child = ChildName(rank, name, births)
    boy_names_object_list.append(new_child)

girl_names_object_list = []
for line in girl_names_file_list:
    line = line.split()
    rank = line[0]
    name = line[1]
    births = line[2]
    new_child = ChildName(rank, name, births)
    girl_names_object_list.append(new_child)


#Game logic: while player has said that they would like to continue, the game will asking them
#which name was more popular based on births.

correct_guess = 0
total_guess = 0
continue_option = "y"
while continue_option == "y":
    # randomly chooses an object from the girl and boy lists
    girl = random.choice(girl_names_object_list)
    boy = random.choice(boy_names_object_list)

    # Question and choice print statement
    print(f"In 2015, was the name {girl.name} (1) or {boy.name} (2) more popular? (enter 1 or 2)")
    choice = int(input())

    # Check for valid input
    while int(choice) not in (1, 2):
        choice = int(input("Invalid option, choose 1 or 2: "))

    # calls choice_checker function to determine guess and then outputs the corresponding statement
    stored_result = choice_checker(girl, boy, choice)
    if stored_result == True:
        print(f"Correct! There were {girl.births} girls named {girl.name}, and {boy.births} boys named {boy.name} ")
        correct_guess += 1
        total_guess += 1
    else:
        print(f"Incorrect. There were {girl.births} girls named {girl.name}, and {boy.births} boys named {boy.name} ")
        total_guess += 1
    
    # determines if playing again, checking for either Y/y or N/n
    print("Play again (y/n)")
    continue_option = input()
    while continue_option not in ("Y", "y", "N", "n"):
        continue_option = input("Invalid choice, choose y or n: ")
    
    #if yes continue game, if no prints guess %
    if continue_option == "n":
        print(f'You had a {(correct_guess/total_guess * 100):.2f}% guess rate!')