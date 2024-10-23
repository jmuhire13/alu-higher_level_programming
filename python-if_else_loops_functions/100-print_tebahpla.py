#!/usr/bin/python3

def print_tebahpla():
    for i in range(26):
        print(chr(122 - i + (i % 2) * 32), end='')

print_tebahpla()
