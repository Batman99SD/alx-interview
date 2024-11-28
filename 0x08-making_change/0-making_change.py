#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""Solution to make changes problem"""


def makeChange(coins, total):
    """
    Function to make change for a given total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for i in range(1, total + 1):

        for j in coins:

            if j <= i:

                dp[i] = min(dp[i], dp[i - j] + 1)

    return -1 if dp[total] > total else dp[total]
>>>>>>> fa99d61dc2d5550689adfa9edf0f383acd0d7277
