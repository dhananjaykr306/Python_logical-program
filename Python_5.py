"""
5. Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
Input: nums = [4,1,2,1,2]
Output: 4
"""

'''
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program to find the single number that appears only once in an array.
'''

def single_number(nums):
    """
    Description : This function takes an array of integers as input and returns the single number that appears only once.
    return : The single number that appears only once.
    """
    for i in nums:
        if nums.count(i) == 1:
            return i
    
def main():
    nums = [4,1,2,1,2]
    print("",single_number(nums))

if __name__ == "__main__":
    main()