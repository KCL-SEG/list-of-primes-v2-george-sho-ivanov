"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from ast import increment_lineno
from re import T


def primes(number_of_primes):
    list = []
    if (number_of_primes <= 0):
        raise ValueError
    list.append(2)
    if (number_of_primes == 1):
        return list
    list.append(3)
    #while list isnt full
    incrementer = 0
    while (len(list) < number_of_primes):
        # check odd numbers greater than the last prime found 
        num_to_check = list[len(list)-1] + 2 + incrementer
        if isPrime(num_to_check):
            list.append(num_to_check)
            incrementer = 0
        else:
            incrementer = incrementer + 2
    return list

def isPrime(num):
    for factor in range(2, num-1):
        if (num % factor == 0):
            return False
    return True
