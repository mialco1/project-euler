"""
Title: Multiples of 3 and 5
--------------------------------------------------------------------------------
Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-08
"""
def main():
    sum = 0
    multiples = []

    for n in range(0, 1000, 3):
        multiples.append(n)

    for n in range(0, 1000, 5):
        if(n % 3 != 0):
            multiples.append(n)

    for m in multiples:
        sum += m

    print(sum)


if __name__ == "__main__":
    main()
