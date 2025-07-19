from math import isqrt
from timeit import default_timer as timer
import matplotlib.pyplot as plt

"""
Deprecated Sieve of Eratosthenes Function

def sieve_eratosthenes(n):
    assert isinstance(n, int)
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
"""

def time(func, n):
    start = timer()
    val = func(n)
    end = timer()
    time_difference = end-start
    print(f"Time taken: {time_difference:.7}s for '{func.__name__}'")
    return val, time_difference

def plot(functions: list, max_degree=5):
    assert len(functions) < 10

    # Initialize Dictionary
    result_dict = {}
    for func in functions:
        result_dict[func.__name__] = []

    # Initialize abscissa
    x = []

    # Initialize colors
    color_index = 0
    colors = ['red', 'blue', 'green', 'black', 'brown', 'purple', 'yellow']

    # Get time values
    print("Getting time values...")
    for degree in range(1,max_degree+1):
        value = 10**degree
        x.append(value)
        for func in functions:
            start = timer()
            func(value)
            end = timer()
            realtime = end-start
            result_dict[func.__name__].append(realtime)

    # Plotting
    for func in functions:
        plt.plot(x, result_dict[func.__name__], label=func.__name__, color=colors[color_index], linestyle='-', marker='o')
        color_index+=1

    plt.title("Sieve complexity chart")
    plt.xlabel("Degree of powers")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.xscale('log')
    

    # Show the plot
    plt.show()

def sieve_trial_division(n):
    assert isinstance(n, int)
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

def sieve_eratosthenes(n):
    assert isinstance(n, int)
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

def sieve_sundaram(n):
    assert isinstance(n, int)
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

def sieve_atkin(n):
    assert isinstance(n, int)
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

def atkin_sundaram_inter(step = 10**5):
    for i in range(10**6, 10**7, step):
        if sieve_atkin(i) < sieve_sundaram(i):
            return i

"""
Test out these commands:
"""

#print(sieve_eratosthenes(500))

#time(sieve_trial_division, 1_000_000)
#time(sieve_eratosthenes, 1_000_000)
#time(sieve_sundaram, 1_000_000)
#time(sieve_atkin, 1_000_000)

#plot([sieve_eratosthenes, sieve_sundaram, sieve_atkin, sieve_trial_division], 7)
#plot([sieve_sundaram, sieve_atkin], 8)

#print(f"Sundaram < Atkin from n = {atkin_sundaram_inter():,}")
