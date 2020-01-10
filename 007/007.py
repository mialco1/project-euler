"""
Title: 10001st prime
--------------------------------------------------------------------------------
Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-09
"""
import math

def is_prime(num):
    if num > 2 and num % 2 == 0:
        return False

    # Can skip even numbers
    # Only need to check values that are less than num / 2
    for x in range(2, math.floor(num / 2), 2):
        if(num % x == 0):
            return False

    return True


def main():
    count = 0
    n = 1

    while count < 10001:
        n += 1 # This will make n = 2 on first pass
        if is_prime(n):
            count += 1

    print(n)


if __name__ == "__main__":
    main()
