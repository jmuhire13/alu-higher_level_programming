#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from the add_0 module
    from add_0 import add

    # Assign values to a and b
    a = 1
    b = 2

    # Use string formatting to print the result
    print("{} + {} = {}".format(a, b, add(a, b)))
