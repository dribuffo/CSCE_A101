'''You have a list of numbers, number_list, that contains both odd and even integers. How can you create
two separate lists, odd_numbers and even_numbers, to store the odd and even integers from
number_list, respectively?'''

#initializing number_list, odd_numbers, and even_numbers to empty lists
number_list = [10, 7, 15, 9, 12] #length = 5
odd_numbers = []
even_numbers = []

x = 0
while(x < len(number_list)):
    #determining odd or even
    if (number_list[x] % 2) == 0:
        #if even number add to even number list
        even_numbers.append(number_list[x])
    else:
        #if odd number add to odd number list
        odd_numbers.append(number_list[x])
    x += 1

print(f'Even numbers: {even_numbers}')
print(f'Odd numbers {odd_numbers}')