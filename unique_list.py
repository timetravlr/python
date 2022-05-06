#!/usr/env/python3
# Practice borrowed from udemy course: python bootcamp

# Write a python function taking a list and returning a new list with unique elements of the first list.

# create a variable called seen_numbers, then append into it
def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers
    
print(unique_list([1,1,1,1,2,2,3,3,3,4,5,7]))


