"""
13.Given a text and a pattern, return the index of the first occurrence of pattern
in text and return -1 if pattern is not part of text.
Input: text = 'ABCABAABCABAC', pattern = 'ABAA'
Output: 3
Explanation: The pattern occurs only once in the text, starting from index 3.
Input: text = 'ABCABAABCABAC', pattern = 'CAB'
Output: 2
Explanation: The pattern occurs twice in the text, starting from index 2 and 8. The solution should return
the index of the first occurrence, i.e., 2.
"""

'''
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program to find the starting index of the first occurrence of a pattern in a given text
'''

def find_pattern(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            return i + 1
    return -1

def main():
    text = 'ABCABAABCABAC'
    pattern = 'ABAA'
    print(find_pattern(text, pattern))

if __name__ == '__main__':
    main()
