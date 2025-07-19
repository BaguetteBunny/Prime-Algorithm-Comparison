from math import isqrt

def sieve_trial_division(n: int):
    assert n>1

    primes = [2]

    for number in range(3, n+1, 2):
        limit = isqrt(number)
        is_prime = True
        for p in primes:
            if p>limit:
                break
            if number%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes