#!/usr/bin/python3
for i in range(10):  # Loop for the first digit
    for j in range(i + 1, 10):  # Loop for the second digit
        print("{:01d}{:01d}".format(i, j),
              end=", " if i < 8 else "\n")
