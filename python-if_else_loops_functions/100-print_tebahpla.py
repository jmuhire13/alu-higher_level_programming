#!/usr/bin/python3

def print_tebahpla():
    print(''.join(chr(122 - i + (i % 2) * 32) for i in range(26)), end='')

print_tebahpla()
