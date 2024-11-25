""" 
10. Run–length encoding (RLE) is a simple form of lossless data compression that
runs on sequences with the same value occurring many consecutive times. It
encodes the sequence to store only a single value and its count.
Input:
'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
Output: '12W1B12W3B24W1B14W'
Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and soon.
"""

""" 
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program to implement Run-length encoding (RLE)
"""

def run_length_encoding(string):
    """
    Description: This function takes a string as input and returns the run-length encoding of the string.
    return: The run-length encoding of the string.
    """
    result = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            result += str(count) + string[i-1]
            count = 1
    result += str(count) + string[-1]
    return result

def main():
    """
    Description: This function is the main function which is used to call the run_length_encoding function.
    return : the run-length encoding of the string.
    """
    string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    print(run_length_encoding(string)) # Output: '12W1B12W3B24W1B14W'

if __name__ == '__main__':  
    main()