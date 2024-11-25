"""
2.Reverse Integer:
Input= 123
output: 321
Input: -4576
output: -6754
"""
'''
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program to reverse an integer.
'''
def reverse(n):
    """
    Description: This function takes an integer as input and returns the reverse of the integer.
    return: The reverse of the integer.
    """
    if n < 0:
        n = -n
        n = int(str(n)[::-1])
        n = -n
    else:
        n = int(str(n)[::-1])
    return n

def main():
    n = int(input("Enter a number: "))
    x=reverse(n)
    print("Reverse of number is: ",x)

if __name__ == "__main__":
    main()