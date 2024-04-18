# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200112
#!244.py
# ------------------------------
"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
then [6, 9, 12, ...] (multiples of three), and so on. 
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""


def sieve_eratosthenes(N):
    """return all primes less than N by Sieve of Eratosthenes algorithm"""
    print(N)
    if N < 3:
        return []
    else:
        primes = [i for i in range(2, N)]  # initilize full-range output list
        # after Sieve of Eratosthenes, list 'primes' contains only prime numbers
        for i in range(2, N // 2 + 1):
            j = 2  # multiple
            while j * i < N:
                if j * i in primes:
                    primes.remove(j * i)
                j += 1
        return primes


def test_sieve_eratosthenes():
    assert sieve_eratosthenes(2) == []
    assert sieve_eratosthenes(3) == [2]
    assert sieve_eratosthenes(4) == [2, 3]
    assert sieve_eratosthenes(10) == [2, 3, 5, 7]


if __name__ == "__main__":
    test_sieve_eratosthenes()
