'''You have a string variable named my_string containing the text "CSCE 101". How can you create a new
string variable reversed_string that stores the reverse of my_string?'''

my_string = "CSCE 101"

# 8 characters long
my_string_length = len(my_string) 

#start at position[7] (len-1) go to [0] and extract that letter at that position 
#and append to reversed_string
reversed_string = my_string[my_string_length::-1] 

print(reversed_string) 

print("")
# this is the long way of doing it but I'm not sure which version 
# is acceptable for this assignment.
other_reversed_string = my_string[-1] + my_string[-2] + my_string[-3] + my_string[-4] + my_string[-5] + my_string[-6] + my_string[-7] + my_string[-8]

print(other_reversed_string)