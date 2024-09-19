#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    """
    if total <= 0:
        return 0
    test = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while test < total:
            test += i
            temp += 1
        if test == total:
            return temp
        test -= i
        temp -= 1
    return -1
