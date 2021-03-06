"""
Title: Largest palindrome product
--------------------------------------------------------------------------------
Description:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
--------------------------------------------------------------------------------
Author: Michael A. Colon
Date: 2020-JAN-09
"""
def is_palindrome(n):
	n_string = str(n)
	reverse_string = n_string[::-1]

	if n_string == reverse_string:
		return True

	return False


def main():
    palindrome = -1

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            v = i * j
            if is_palindrome(v):
                if (v) > palindrome:
                    palindrome = v

    if(palindrome == -1):
        print("Palindrome not found!")
    else:
        print(palindrome)


if __name__ == "__main__":
    main()
