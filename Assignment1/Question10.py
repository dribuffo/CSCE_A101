'''You have been introduced to the fundamentals of Python programming in the first three weeks of the
Fall 2023 semester, including introduction to Python, variables and expressions, input/output, and
datatypes. In this exercise, you have the opportunity to showcase your understanding by writing any
Python program of your choice. You are also free to use any Python features in this problem statement,
even If it is not covered yet. '''

### ADVENTURE STORY CREATOR ###
import random

### Story Functions ###
def cursed_tomb_adventure(adventuring_team):
    adventuring_log = [
                ' was eaten by a monster.',
                ' found the hidden treasure of Olmec worth 10 gold, and +1 to their wisdom stat.',
                ' couldnt find his torch and fell into a pit of snakes.',
                ' was too scared to enter and waited outside.',
                ' got lost in the maze and succumbed to hunger after a while.',
                ' found the Cursed Tomb and was rewarded with riches beyond their wildest dream.',
            ] 
    random.shuffle(adventuring_team)
    random.shuffle(adventuring_log)

    for index in range(len(adventuring_team)):
        print(f'{adventuring_team[index][0]} the {adventuring_team[index][1]}' + adventuring_log[index])

def ocean_adventure(adventuring_team):
    adventuring_log = [
                ' saved the King of the Seas and got his treasure of 1000 carp.',
                ' fell into the water when the ship ran into a storm.',
                ' found a mansion on the mysterious island and decided to retire there. Lose 100 gold.',
                " found the Pirate King's treasure; Oddly, it was all in one piece.",
                ' ran the ship into a storm and somehow found themselves back at the starting port.',
                ' was in the tavern drinking grog and missed the ship setting sail.',
                ' was promoted to boatswain. Hey, congrats! +1 to Strength stat.',
            ] 
    random.shuffle(adventuring_team)
    random.shuffle(adventuring_log)

    for index in range(len(adventuring_team)):
        print(f'{adventuring_team[index][0]} the {adventuring_team[index][1]}' + adventuring_log[index])

def mad_wizards_tower(adventuring_team):
    adventuring_log = [
                ' was turned into a monster by the Mad Wizard.',
                ' found the forbidden library of the Mad Wizard. Gain +1 to intelligence.',
                " got stuck in the maze of the neverending staircase. Some say they're still climbing to this day.",
                " couldn't find the secret entrance and decided to wait outside.",
                ' fell into a trap and was stuck cleaning the tower forever... and ever... and ever...',
                ' defeated the Mad Wizard and saved the kingdom! As a reward the King gave them 1000 gold.',
            ] 
    random.shuffle(adventuring_team)
    random.shuffle(adventuring_log)

    for index in range(len(adventuring_team)):
        print(f'{adventuring_team[index][0]} the {adventuring_team[index][1]}' + adventuring_log[index])

# take in team size from the user
team_size = int(input("How big is your adventuring party? Max of 4. "))
if team_size >= 5:
    print("Invalid team size. Guess you didn't want to go on an adventure today...")
else:
    # name team members and give them jobs
    adventuring_team = []
    for unit in range(team_size):
        character_name = input("What is this character's name? ")
        character_job = input("What is this character's job? ")
        adventuring_team.append([character_name, character_job])

    # prints available adventures
    print(
        '''
        Adventure 1: Cursed Tomb
        Adventure 2: Ocean Adventure
        Adventure 3: Mad Wizard's Tower
        '''
        )
    # let user choose adventure they want to take
    chosen_adventure = int(input("What adventure would you like to send your team on? "))
    print(" ")

    # calls appropriate function to determine what happened and then displays results
    match chosen_adventure:
        case 1:
            cursed_tomb_adventure(adventuring_team)
        case 2:
            ocean_adventure(adventuring_team)
        case 3:
            mad_wizards_tower(adventuring_team)
        case _:
            print("You have chosen... poorly. Adventure Team has disbanded and taken your money.")