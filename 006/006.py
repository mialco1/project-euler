"""
Title: Sum square difference
--------------------------------------------------------------------------------
Description:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-09
"""
def main():
    sum_of_squares = 0
    squared_sum = 0

    for n in range(1, 101):
        sum_of_squares += n**2

    for n in range(1, 101):
        squared_sum += n

    squared_sum = squared_sum ** 2
    
    print(squared_sum - sum_of_squares)


if __name__ == "__main__":
    main()
