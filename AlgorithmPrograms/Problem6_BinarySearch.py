"""BinarySearch program read in a list of words from File. Then prompt the user to enter a word to
search the list. The program reports if the search word is found in the list or not.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""

# importing important modules
import utility.Utility
import string

open_file = open("binary.txt")  # opening text file named "binary.txt"
sen_split = list(open_file.read().split())  # adding each word of every sentence to the list "sen_split" as an item
word = [word.strip(string.punctuation) for word in sen_split]  # trimming all commas/punctuation present in the sentence
utility.Utility.insertion_sort(word)  # sorting the comma/punctuation trimmed list using user-defined function

user_input = input("\nEnter your word to search in the file: ")

res = utility.Utility.binary_search(word, user_input)  # searching the user-input string in the sorted list "word"
# using user-defined function "binary_search" which @return boolean value having @param list and @string to search

if res:
    print("\nYes, '%s' is present in the file." % user_input)
else:
    print("\nNo, %s is not present in the file." % user_input)

