#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
str1 = input("Enter a word")
str2 = input("Enter a word")
str3 = input("Enter a word")
str4 = input("Enter a word")
str5 = input("Enter a word")

words = [str1, str2, str3, str4, str5]

print(words)