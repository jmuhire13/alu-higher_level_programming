#!/usr/bin/python3
for i in range(97, 123):  # ASCII range for lowercase letters
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
