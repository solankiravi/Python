from collections import Counter

word1='abcd'
word2='dcab'

def is_palindrome_1(word1: str, word2: str):
    if(len(word1) != len(word2)):
        return False
    temp_word1,temp_word2 = sorted(word1), sorted(word2)
    for index,value in enumerate(temp_word1):
        if(temp_word1[index] != temp_word2[index]):
            return False
    return True

def is_palindrome_2(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    return Counter(word1) == Counter(word2)

is_palindrome_1(word1,word2)