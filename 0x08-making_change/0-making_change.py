#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed

    Args:
        coins (List): List of the values of the coins.
        total (int): total amount
    """
    if total <= 0:
        return 0
    amount = 0
    tmp = 0
    coins.sort(reverse=True)
    for coin in coins:
        while amount < total:
            amount += coin
            tmp += 1
        if amount == total:
            return tmp
        amount -= coin
        tmp -= 1
    return -1
