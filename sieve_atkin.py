from math import isqrt

def sieve_atkin(n: int):
    assert n>=0

    if n < 2:
        return []
    if n < 3:
        return [2]

    n+=1
    prime_list = [2,3]
    is_prime = [False]*n

    # 3.1 If r is 1, 13, 17, 29, 37, 41, 49, or 53, flip the entry for each possible solution to 4x2 + y2 = n
    for x in range(1, isqrt(n//4)+2):
        xx4 = 4*x**2
        for y in range(1, isqrt(n)+2, 2):
            eq = xx4 + y**2
            if eq >= n:
                break
            if eq % 12 == 1 or eq % 12 == 5:
                is_prime[eq] = not is_prime[eq]
    
    # 3.2 If r is 7, 19, 31, or 43, flip the entry for each possible solution to 3x2 + y2 = n
    for x in range(1, isqrt(n//3)+2, 2):
        xx3 = 3*x**2
        for y in range(2, isqrt(n)+2, 2):
            eq = xx3 + y**2
            if eq >= n:
                break
            if eq % 12 == 7:
                is_prime[eq] = not is_prime[eq]

    # If r is 11, 23, 47, or 59, flip the entry for each possible solution to 3x2 − y2 = n when x > y
    for x in range(2, isqrt(n//2)+2):
        xx3 = 3*x**2
        for y in range(x-1, 0, -2):
            eq = xx3 - y**2
            if eq >= n:
                break
            if eq % 12 == 11:
                is_prime[eq] = not is_prime[eq]

    # Remove multiples of squares
    for i in range(5, isqrt(n)):
        if is_prime[i]:
            for j in range(i*i, n, i*i):
                is_prime[j] = False

    # Collection
    for i in range(5, n, 2):
        if is_prime[i]:
            prime_list.append(i)
    
    return prime_list