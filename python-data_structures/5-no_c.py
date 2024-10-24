#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the new string
    new_string = ""
    # Loop through each character in the original string
    for char in my_string:
        # If the character is not 'c' or 'C', add it to the new string
        if char != 'c' and char != 'C':
            new_string += char
    # Return the new string without 'c' or 'C'
    return new_string
