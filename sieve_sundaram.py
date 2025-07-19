from math import isqrt

def sieve_sundaram(n: int):
    assert n>=0

    if n < 2:
        return []
    
    n+=1
    prime_list = [2]
    is_prime = [True]*n
    new_n = int((n-1)/2)

    # Mark all numbers of the form i + 2ij + j
    for i in range(1, isqrt(new_n)+1):
        max_j = (new_n - i) // (2 * i + 1)+1
        for j in range(i, max_j):
            ij2ij = i + j + 2 * i * j
            if ij2ij > new_n:
                break
            is_prime[ij2ij] = False

    # Return all non-marked numbers N where 2n+1 is Prime
    for i in range(1, new_n):
        if is_prime[i]:
            prime_list.append(2*i+1)

    return prime_list