#!/usr/bin/python3
"""
Module 0-making_change
"""

def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    # Set the list size to total + 1, and initialize each element to infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Compute the minimum coins required for each amount up to total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total amount is still infinity, it means it's not possible to
    # make that amount
    return dp[total] if dp[total] != float('inf') else -1
