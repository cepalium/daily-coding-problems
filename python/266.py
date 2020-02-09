# ---------------------------------
# Author: Tuan Nguyen
# Date created: 20200209
#!266.py
# ---------------------------------
"""
A step word is formed by taking a given word, adding a letter, and anagramming the result. 
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, 
create a function that returns all valid step words.
"""
import string

def step_words(words, input_word):
    """ return list of all valid step words from input word """
    valid = []    # output list of valid step words
    for word in words:
        if len(input_word) - len(word) != 1:    # current word cannot be added 1 letter to be a valid step word
            continue
        freq_input = letter_frequency(input_word)
        freq_cur = letter_frequency(word)
        diff = 0    # sum of different no. each letters in current word & input word
        for c in freq_input.keys():
            diff += abs(freq_input[c] - freq_cur[c])
        if diff == 1:    # current word needs to add 1 letter to be valid step word
            valid.append(word)
    return valid        

def letter_frequency(word):
    """ return a dictionary of each letter frequency from word """
    freq_letter = {c: 0 for c in string.ascii_lowercase}
    for c in word:
        if c not in freq_letter.keys():
            freq_letter[c] = 1
        else:
            freq_letter[c] += 1
    return freq_letter

def test1():
    assert step_words(words=['apple', 'pear', 'lemon', 'paple'], input_word='appeal') == ['apple', 'paple']

def test2():
    assert step_words(words=['a', 'ab', 'abc', 'abcd', 'abcde'], input_word='abcd') == ['abc']

if __name__ == "__main__":
    test1()
    test2()