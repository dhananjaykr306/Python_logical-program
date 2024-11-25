"""
10.Given an integer array, in-place reverse it without using any inbuilt functions.
Input : [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

"""
    @Author: Dhananjay Kumar
    @Date: 25-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 25-11-2024
    @Title: Python program to reverse an array in-place without using any inbuilt functions.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def main():
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    arr = reverse_array(arr)
    print("Reversed array:", arr)

if __name__ == '__main__':
    main()