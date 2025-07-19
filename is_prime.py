from timeit import default_timer as timer
from math import isqrt, sqrt

PRIME_LIST = {
  "10^1": 7,
  "10^2": 97,
  "10^3": 997,
  "10^4": 9973,
  "10^5": 99991,
  "10^6": 999983,
  "10^7": 9999991,
  "10^8": 99999989,
  "10^9": 999999937,
  "10^10": 9999999967,
  "10^11": 99999999977,
  "10^12": 999999999989,
  "10^13": 9999999999971,
  "10^14": 99999999999973,
  "10^15": 999999999999989,
  "10^16": 9999999999999937,
}

# Calculating time for one set of values
def unique_test(func, max, print_final=True, print_details=False):
    max_dict = PRIME_LIST if max == -1 else {k: PRIME_LIST[k] for k in list(PRIME_LIST)[:max]}

    final_start = timer()
    for key, value in max_dict.items():
        start = timer()
        check_prime = func(value, isqrt(value)+1)
        end = timer()
        if not check_prime:
            print("Error: Not prime. Passing to next number...")
            continue
        if print_details:
            print(f"Verified at <{key} in {end-start:.10f}s")
    final_end = timer()
    
    if print_final:
        print(f"Total time taken: {final_end-final_start:.10f}s")

# Calculating average time of quantity times unique tests
def average_test(func, max, quantity=100, return_times=False):
    total_times = []
    for i in range(quantity):
        average_start = timer()
        unique_test(func, max, print_final=False, print_details=False)
        average_end = timer()
        total_times.append(average_end-average_start)

    print(f"Average time at {quantity} iterations is: {sum(total_times)/len(total_times)}")
    if return_times:
        return total_times

# Calculating confidence interval of quantity times unique tests
def confidence_interval(func, max, quantity=100, decimal_places=9):
    times = average_test(func, max, quantity, return_times=True)

    mean = sum(times)/quantity
    variance = sum([(x - mean) ** 2 for x in times])/(quantity-1)
    std_dev = sqrt(variance)

    margin_of_error = 1.96*(std_dev/sqrt(quantity))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    print(f"With 95% confidence, the true average runtime of '{func.__name__}' in seconds is within I = [{lower_bound:.{decimal_places}f} ; {upper_bound:.{decimal_places}f}]")

# Classic Prime Computing
def classic_isprime(n, _=None):
    if n <= 1:
        return False
    else:
        for possible_divisor in range(2, isqrt(n)+1):
            if n % possible_divisor == 0:
                return False
        return True

# Recursive Prime Computing
def recursive_isprime(n, i):
    if i == 2:
        return True
    if n%i == False:
        return False
    if recursive_isprime(n, i - 1) == False:  
        return False
    return True

"""
At 10^5, q=100_000:
    Classic Prime: [0.0000104 ; 0.0000105]
    Recursive Prime: [0.0000377 ; 0.0000378]
"""

"""
Test out these commands:
"""

#print(classic_isprime(PRIME_LIST["10^12"]))
#print(recursive_isprime(PRIME_LIST["10^13"]))

#unique_test(classic_isprime, -1, 1000, print_details=True)
#unique_test(recursive_isprime, -1, 1000, print_details=True)

#confidence_interval(classic_isprime, 5, 100_000)
#confidence_interval(recursive_isprime, 5, 100_000)