# Copyright 2016-2023 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Boring Math integer library

Library of functions of an integer pure math nature.
"""

from __future__ import annotations

import sys
from typing import Iterator, Tuple
from grscheller.circular_array import CircularArray

__all__ = ['gcd', 'lcm', 'mkCoprime', 'primes', 'comb',
           'pythag3', 'ackermann', 'fibonacci']

# Number Theory mathematical Functions.

def gcd(fst: int, snd: int) -> int:
    """Uses Euclidean algorithm to compute the gcd of two integers

    Takes two integers, returns gcd >= 0.

    Note: gcd(0,0) returns 0 but in this case the gcd does not exist
    """
    fst, snd = abs(fst), abs(snd)
    fst, snd = (fst, snd) if fst > snd else (snd, fst)
    while snd > 0:
        fst, snd = snd, fst % snd

    return fst

def lcm(fst: int, snd: int) -> int:
    """Finds the least common multiple of two integers.
       Takes two integers, returns lcm >= 0.
    """
    common = 1 if 0 == fst == snd else gcd(fst, snd)
    fst //= common

    return abs(fst*snd)

def mkCoprime(fst: int, snd: int) -> Tuple(int, int):
    '''Makes 2 integers coprime by dividing out their common factors.

       Note: One use case is when dividing two factored BigInts. This is the main
             motivation for choosing mkCoprime(0, 0) = (0, 0) instead of (1, 1).
    '''
    common = 1 if 0 == fst == snd else gcd(fst, snd)
    return fst // common, snd // common

def primes(start: int=2, end_before: int=100) -> Iterator:
    """Return an iterator for the prime numbers Using the Sieve of Eratosthenes
    algorithm.
    """
    if start >= end_before or end_before < 3:
        return []
    if start < 2:
        start = 2

    sieve = [x for x in range(3, end_before, 2) if x % 3 != 0]
    stop = int(end_before**(0.5)) + 1
    front = -1
    for prime in sieve:
        front += 1
        if prime > stop:
            break
        for pot_prime in sieve[-1:front:-1]:
            if pot_prime % prime == 0:
                sieve.remove(pot_prime)

    if start <= 3 < end_before:  # We missed [2, 3] but
        sieve.insert(0, 3)       # saved about 60% for
    if start <= 2 < end_before:  # the initial storage
        sieve.insert(0, 2)       # space.

    # return sieve after trimming unwanted values
    return (x for x in sieve if x >= start)

# Combinatorics

def comb(n: int, m: int, factorsNumerator: int=66, factorsDenominator: int=4) -> int:
    """Implements C(n,m), the number of combinations of n items taken m at a time,
    in a way that works efficiently for Python's arbitrary length integers. Compares
    well with math.comb() which is probably C code.

    Raises: ValueError if n < 0 or m < 0
    """
    if n < 0 or m < 0:
        raise ValueError('for C(n, m) n and m must be a non-negavive ints')
    if n == m or m == 0:
        return 1
    elif m > n:
        return 0

    # using C(n, m) = C(n, n-m) to reduce number of factors in calculation
    if m > (n // 2):
        m = n - m

    def compact(ca: CircularArray, targetSize: int) -> CircularArray:
        """Reduce the length of the circular array by factors of 2 by
        combinding factors from each end, O(ln(n)).
        """
        ca1 = ca
        while len(ca1) > targetSize:
            ca2 = CircularArray()
            size = len(ca1)
            if size % 2 == 1:
                ca1.pushR(ca1.popL() * ca1.popR())
                size -= 1
            for ii in range(size // 2):
                ca2.pushL(ca1[ii] * ca1[size - ii - 1])
            ca1 = ca2
        return ca1

    # Prepare data structures
    topFactors = CircularArray(*range(n - m + 1, n + 1))
    bottomFactors = CircularArray(*range(m, 1, -1))

    # Compact data structures
    topFactors = compact(topFactors, factorsNumerator)
    bottomFactors = compact(bottomFactors, factorsDenominator)

    # Cancel all factors in denominator before multiplying
    # the remaining factors in the numerator.
    for bottom in bottomFactors:
        for ii in range(len(topFactors)):
            top, bottom = mkCoprime(topFactors.popL(), bottom)
            if top > 1:
                topFactors.pushR(top)
            if bottom == 1:
                break

    return topFactors.foldL(lambda x, y: x * y)

# Pythagorean Triples

def pythag3(a_max: int=3, all_max: int|None=None) -> Iterator:
    """This iterator finds all primative pythagorean triples
    up to a given level.  A Pythagorean triple are three
    integers (a,b,c) such that a^2 + b^2 = c^2 where
    x,y,z > 0 and gcd(a,b,c) = 1

    If called with one argument, generates all triples with
    a <= a_max

    If called with two arguments generate all triples with
    a <= a_max and a,b,c <= all_max
    """
    def cap_max_abc(a_max: int, all_max: int=None) -> int:
        """Returns capped max values for sides a,b,c where
        based on a_max and all_max given by caller of pythag3.

        note: a_max and c_max are integers
        note: b_max is a function of side a
        """
        # Limit values to those where geometry
        # based optimization assumptions hold.
        if a_max < 3:
            a_max = 2

        # For a given value of a, theoretically there
        # are no more triples beyond this value of b.
        def b_max_uncapped(a):
            return (a**2 - 1)//2

        if all_max is None:
            b_max = b_max_uncapped
        else:
            if all_max < 5:
                all_max = 4
            if all_max < a_max + 2:
                a_max = all_max - 2

            def b_max_capped(a):
                return min((b_max_uncapped(a), int((all_max**2 - a**2)**0.5)))

            b_max = b_max_capped

        c_max = int((a_max**2 + b_max(a_max)**2)**(0.5)) + 1

        return a_max, b_max, c_max

    # Cap triples to those with sides no bigger than all_max
    a_max, b_max, c_max = cap_max_abc(a_max, all_max)

    # Hypothrnuse perfect square lookup dictionary
    # Note: hypotenuse always odd for Pythagorean triples
    squares = {h*h: h for h in range(5, c_max + 1, 2)}

    # Calculate Pythagorean triples
    for side_a in range(3, a_max + 1):
        for side_b in range(side_a + 1, b_max(side_a) + 1):
            csq = side_a**2 + side_b**2
            if csq in squares:
                if gcd(side_a, side_b) == 1:
                    yield side_a, side_b, squares[csq]

# Computable but not primitive recursive functions

def ackermann(m: int, n:int) -> int:
    """Ackermann function is defined recursively by:

    ackermann(0,n) = n+1
    ackermann(m,0) = ackermann(m-1,1)
    ackermann(m,n) = ackermann(m-1, ackermann(m, n-1)) for n,m > 0

    Ackerman's function is an example of a function that is computable
    but not primatively recursive. It quickly becomes computationally
    intractable for relatively small values of m and n.
    """
    # Model a function stack with a list, then
    # evaluate innermost ackermann function first.
    acker = [m, n]

    while len(acker) > 1:
        mm, nn = acker[-2:]
        if mm < 1:
            acker[-1] = acker.pop() + 1
        elif nn < 1:
            acker[-2] = acker[-2] - 1
            acker[-1] = 1
        else:
            acker[-2] = mm - 1
            acker[-1] = mm
            acker.append(nn-1)

    return acker[0]

# Fibonacci Iterator

def fibonacci(fib0: int, fib1: int) -> Iterator:
    """Returns an iterator to a Fibonacci sequence whose
    first two terms are fib0 and fib1.
    """
    while True:
        yield fib0
        fib0, fib1 = fib1, fib0+fib1

if __name__ == '__main__':
    sys.exit(0)
