#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Check if idx is within valid range
    if 0 <= idx < len(my_list):
        # Replace the element at the given index
        new_list[idx] = element
    
    # Return the new list (either modified or the original copy)
    return new_list
