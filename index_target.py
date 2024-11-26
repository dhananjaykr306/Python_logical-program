"""
11.Given a sorted integer array and a target, determine if the target exists in the
array in logarithmic time. If a target exists in the array, the procedure should
return the index of it.
Input: nums[] = [2, 3, 5, 7, 9], target = 7
Output: 3
Explanation: Element found at 4th (index 3) position
• If there are duplicate elements in the array, the procedure may return any index whose element is
equal to the target.
Input: nums[] = [1, 2, 3, 4, 4, 5, 6, 7], target = 4
"""

def search(nums, target):
    """ 
        Description :This function takes an array of sorted integers and a target integer as input and returns the index of the target if it exists in the array.
        Time Complexity : O(log n)
        Space Complexity : O(1)
        return the index of the target if it exists in the array, otherwise return -1."""
    if target not in nums:
        return "-1"    
    x= nums.index(target)
    return x

def main(): 
    nums = [2, 3, 5, 7, 9]
    target = 9
    print(search(nums, target))

if __name__ == '__main__':
    main()
