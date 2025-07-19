from timeit import default_timer as timer
import matplotlib.pyplot as plt
from typing import Callable

from sieve_atkin import *
from sieve_sundaram import *
from sieve_eratosthenes import *
from trial_division import *

def time(func: Callable, n: int):
    start = timer()
    val = func(n)
    end = timer()
    time_difference = end-start
    print(f"Time taken: {time_difference:.7}s for '{func.__name__}'")
    return val, time_difference

def plot(functions: list[Callable], max_degree: int =5):
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

def atkin_sundaram_inter(step: int = 10**5):
    for i in range(10**6, 10**7, step):
        if sieve_atkin(i) < sieve_sundaram(i):
            return i

"""
Test out these commands:

print(sieve_eratosthenes(500))

time(sieve_trial_division, 1_000_000)
time(sieve_eratosthenes, 1_000_000)
time(sieve_sundaram, 1_000_000)
time(sieve_atkin, 1_000_000)

plot([sieve_eratosthenes, sieve_sundaram, sieve_atkin, sieve_trial_division], 7)
plot([sieve_sundaram, sieve_atkin], 8)

print(f"Sundaram < Atkin from n = {atkin_sundaram_inter():,}")
"""