"""
1.Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
'''
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

def twoSum(nums, target):
     """
        Description:
            This function is used to find the indices of the two numbers such that they add up to target.
        Return:
            return the indices of the two numbers such that they add up to target.
    """
     for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([2,7,11,15], 9))
