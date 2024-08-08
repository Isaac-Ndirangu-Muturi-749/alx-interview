#!/usr/bin/python3
"""
Module 0-prime_game
"""


def sieve_of_eratosthenes(max_n):
    """Generate a list of prime numbers up to max_n
    using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes, is_prime


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes, is_prime = sieve_of_eratosthenes(max_n)

    def count_primes_up_to(n):
        return sum(is_prime[:n + 1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if count_primes_up_to(n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
