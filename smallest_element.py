"""
9.Given an integer array, find k'th smallest element in the array where k is a
positive integer less than or equal to the length of array.
Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4
Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
Output: 4
Explanation: The 5th smallest array element is 4
    @Author: Dhananjay Kumar
    @Date: 25-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 25-11-2024
    @Title: Python program to find the kth smallest element in an array
"""

def kth_smallest_element(arr, k):
    """ 
    Description: This function takes an array and a positive integer k as input and returns the kth smallest element in the array.
    Args:
        arr: list, an integer array
        k: int, a positive integer less than or equal to the length of array
    Returns:
        kth_smallest: int, the kth smallest element in the array
    """
    arr.sort()
    kth_smallest = arr[k-1]
    return kth_smallest

def main():
    arr = [7, 4, 6, 3, 9, 1]
    k = 3
    kth_smallest = kth_smallest_element(arr, k)
    print(f"The {k}th smallest element in the array is {kth_smallest}")

if __name__ == "__main__":
    main()
