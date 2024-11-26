"""
3.For a given sentence, return the average word length.
Note: Remember to remove punctuation first.
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
    @Author: Dhananjay Kumar
    @Date: 23-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 23-11-2024
    @Title: Python program to find the average length of words in a sentence.
"""

def average_word_length(sentence):
    """
    Description: This function takes a sentence as input and returns the average word length.
    Input: A string representing a sentence.
    Output: A float representing the average word length.
    """
    # Remove punctuation
    sentence = sentence.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")
    # Split sentence into words
    words = sentence.split()
    # Calculate average word length
    average_length = sum(len(word) for word in words) / len(words)
    return average_length

def main():
    sentence=input("Enter a sentence: ")
    print("The average word length of the sentence is:", average_word_length(sentence))

if __name__ == "__main__":
    main()
