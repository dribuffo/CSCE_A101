'''You are developing a Python program to manage a list of unique usernames. Explain how you can use
sets to ensure that the usernames are unique and to perform operations like adding a new username,
checking for the existence of a username, and removing a username from the list. Provide an example
code snippet to demonstrate these operations using sets.'''

# sets are preferable to use in this instance because they only store unique values in them. 
# If somenoe is attempting to register a new user name and it's in the set already then
# then returning that it's a duplicate is easy. Information within the set is also immutable,
# making sure that the data can't be overwritten without making a new username.

# create fake set of usernames:
usernames = {"CloudStrife", "RamzaBeoulve", "Boko"}

# adding a username:
usernames.add("EmetSelch")

# prints set for reference
print(usernames)

# checking if a username is in the set
searched_name = input("Search for what name? ")
if searched_name in usernames:
    print(f'{searched_name} is already in the set.')
else:
    print(f'{searched_name} is not in the set.')

# removing the username "Boko" from the set
usernames.remove("Boko")

#prints set to show changes
print(usernames)