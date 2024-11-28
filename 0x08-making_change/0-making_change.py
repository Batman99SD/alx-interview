#!/usr/bin/python3
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
