#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up
    to n using the Sieve of Eratosthenes.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determine who the winner is for each round of the game.
    x: number of rounds
    nums: list of n values for each round
    """
    if not nums or x < 1:
        return None
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_removals = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_removals[i] = prime_removals[i - 1] + primes[i]
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_removals[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None