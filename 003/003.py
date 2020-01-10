"""
Title: Largest prime factor
--------------------------------------------------------------------------------
Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-10
"""
import math

def is_prime(num):
    if num <= 0 or (num > 2 and num % 2 == 0):
        return False
    elif num == 2:
        return True

    # Can skip even numbers
    # Only need to check values that are less than num / 2
    for x in range(3, math.ceil(num / 2), 2):
        if(num % x == 0):
            return False

    return True


def get_factors(num):
    factors = [1, num]
    half_value = 0

    # Can start from halfway
    if num % 2 > 0:
        half_value = int(math.floor(num / 2))
    else:
        half_value = int(num / 2)
        factors += [2]
        factors.append(half_value)

    i = 3
    while i < half_value:
        if num % i == 0:
            factors.append(i)
            half_value = num / i

            if(int(half_value) not in factors):
                factors.append(int(half_value))

        i += 1

    factors.sort() # Just for print() purposes
    return factors


def main():
    factors = get_factors(600851475143)
    factors.sort(reverse=True)

    for f in factors:
        if(is_prime(f)):
            print(f)
            break


if __name__ == "__main__":
    main()
