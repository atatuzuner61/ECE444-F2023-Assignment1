#!/usr/local/bin/python3.7

class utils:
    def reversed(x):
        if x != int(x):
            return None

        y = 0
        for i in reversed(range(len(str(x)))):
            y = y * 10 + int(str(x)[i])

        return y

    def formatter(x):
        if x != int(x):
            return None

        return bin(x), oct(x)