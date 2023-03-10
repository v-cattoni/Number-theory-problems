#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:16:57 2022

@author: v-cattoni

This code is to quantify the maximum amount of error involved in using the chinese remainder theorem
to generate twin primes. 

Right now it only finds potential errors that have two prime factors, however the code needs to be 
altered to allow for errors with more than two prime factors.
"""

from math import prod, sqrt
import numpy as np

# generates a list of prime numbers smaller than or equal to pn
# prime_numbers(pn) = [p1, p2, .... , pn]
def prime_numbers(pn):
    primes = []
    for i in range(2, pn + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes


# generates the primorial of n
# primorial(pn) = 2*3* ... *pn
def primorial(pn, prime_numbers):
    primorial_prod = 1
    for i in prime_numbers:
        if i <= pn:
            primorial_prod *= i
    return primorial_prod
 
def main(n):
    
    smaller_primes = prime_numbers(n)
    primo = primorial(n, smaller_primes)
    bigger_primes = prime_numbers(int(primo/n))
    potential_problems = []
    
    for i in smaller_primes:
        bigger_primes.remove(i)
               
    for i in bigger_primes:
        for j in bigger_primes:
            if i*j < primo and [j, i] not in potential_problems:
                potential_problems.append([i,j])

    prod_potential_problems =[]
    for factors in potential_problems:
        prod_potential_problems.append(prod(factors))

    print("")
    print("Number of potential false twins =", len(potential_problems))
    print("")
    print("Potential problems = ", prod_potential_problems)
    print("")
    print("Which are generated by prime factors:", potential_problems)
    print("")
    

    return

main(11)