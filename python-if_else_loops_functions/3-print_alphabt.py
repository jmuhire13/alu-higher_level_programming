#!/usr/bin/python3

for i in range(97, 123):  # ASCII values from 97 ('a') to 122 ('z')
    if chr(i) not in ['e', 'q']:  # Skip 'e' and 'q'
        print(chr(i), end="")  # Print each character without a new line
