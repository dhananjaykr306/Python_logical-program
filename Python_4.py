'''
    @Author: Dhananjay Kumar
    @Date: 25-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 25-11-2024
    @Title: Python program to append the zeroes to the end of the array while maintaining the relative order of the non-zero elements.
'''

"""
4.Given an array nums, write a function to move all zeroes to the end of it while
maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]
Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
"""

def move_zeroes(nums):
    """
    Description: This function takes an array as input and moves all the zeroes to the end of the array while maintaining the relative order of the non-zero elements.
    Returns: the modified array with all zeroes moved to the end.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums

def main():
    nums = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        nums.append(int(input("Enter the element: ")))
    print(move_zeroes(nums))

if __name__ == "__main__":
    main()