"""
8.Given a positive number, check if it is a perfect square without using any
built-in library function. A perfect square is a number that is the square of an
integer.
Input: n = 25
Output: true
Explanation: 25 is a perfect square since it can be written as 5×5.
Input: n = 20
Output: false
    @Author: Dhananjay Kumar
    @Date: 25-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 25-11-2024
    @Title: Python program to check if a number is a perfect square or not
'''

def isPerfectSquare(n):
    if n == 0 or n == 1:
        return True
    i = 1
    while i*i <= n:
        if i*i == n:
            return True
        i += 1
    return False

def main():
    n = int(input("Enter a positive number: "))
    if isPerfectSquare(n):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()
