def isWinner(x, nums):
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    maria_wins, ben_wins = 0, 0

    for n in nums:
        available_numbers = set(range(2, n + 1))
        maria_turn = True
        while available_numbers:
            prime_found = False
            for num in sorted(available_numbers):
                if primes[num]:
                    prime_found = True
                    available_numbers -= set(range(num, n + 1, num))
                    break

            if not prime_found:
                break

            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None