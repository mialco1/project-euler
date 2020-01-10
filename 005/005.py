"""
Title: Smallest multiple
--------------------------------------------------------------------------------
Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-09
"""
def is_divisible(n):
    for x in range (20, 0, -1):
        if n % x != 0:
            return False

    return True

def main():
    number = 0
    checked_value = 20

    while number == 0:
        print("Checking " + str(checked_value) + "...")
        if is_divisible(checked_value):
            number = checked_value

        checked_value += 20

    print(number)


if __name__ == "__main__":
    main()
