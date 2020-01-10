"""
Title: Largest prime factor
--------------------------------------------------------------------------------
Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-09
"""
import math

def is_prime(num):
    if(num % 2 == 0):
        return False

    # Can skip even numbers
    # Only need to check values that are less than num / 2
    for x in range(3, math.floor(num / 2), 2):
        if(num % x == 0):
            return False

    return True


def main():
    print("Hello, world!")


if __name__ == "__main__":
    main()
