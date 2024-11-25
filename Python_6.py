"""
6.Given an array nums of size n, return the majority element.
Input: nums = [3,2,3]
Output: 3
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

"""
    @Author: Dhananjay Kumar
    @Date: 25-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 25-11-2024
    @Title: Python program to find the majority element in an array
"""

def majorityElement(nums):
    """
    Description: This function takes an array of integers as input and returns the majority element in the array.
    return: The majority element in the array.
    """
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict:
        if dict[i] > len(nums)//2:
            return i

def main():
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))

if __name__ == "__main__":
    main()