#!/usr/bin/python3
for i in range(122, 96, -1):
    if (122 - i) % 2:
        i -= 32
    print("{:c}".format(i), end="")
