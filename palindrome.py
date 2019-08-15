"""
File: Palindrome.py
Name:
    
Python program that detects whether 
the given word is a palindrome or not.
Concepts covered: Strings, loops, slicing, if/else
"""
def main():
    #Enter Code Here
    word = input("Enter A Word ")
    word_length = len(word-1)
    if word[0] == word[word_length] and word[1] == word[word_length-1]:
        print ("This Word Is A Palindrome!")
    else:
        print ("This Word Is Not A Palindrome!")
    
    
def Palindrome():
    pass
    

if __name__ == "__main__":
    main()