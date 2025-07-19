from math import isqrt

# Deprecated Sieve of Eratosthenes Function (First attempt)
def deprecated_sieve_eratosthenes(n: int):
    assert n>0

    if n == 1:
        return []
    if n == 2:
        return [2]

    sieve = []
    not_prime = set()
    for number in range(2,n+1):
        if number not in not_prime:
            sieve.append(number)
        for non_prime in range(number,n+1):
            if non_prime%number == 0:
                not_prime.add(non_prime)
    return sieve

def sieve_eratosthenes(n: int):
    assert n>=0

    if n < 2:
        return []

    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False

    for number in range(2,isqrt(n)+1):
        if is_prime[number]:
            for not_prime_index in range(number**2, n+1, number):
                is_prime[not_prime_index] = False
    
    final_primes = []
    for idx, prime in enumerate(is_prime):
        if prime:
            final_primes.append(idx)
    return final_primes