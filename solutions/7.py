# --------------------------
# Author: Tuan Nguyen
# Date created: 20190520
# --------------------------
"""
Problem:

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, 
since it could be decoded as 'aaa', 'ka', and 'ak'.

"""


# libraries
import string 


def mapping():
# output: dictionary table{} (k:v): (1: 'a'), (2: 'b'), ..., (26: 'z')
    table = {}
    alphabet = string.ascii_lowercase     # 'abcdef...xyz'
    i = 1

    # table{} (k:v): (1: 'a'), (2: 'b'), ..., (26: 'z')
    for a in alphabet:
        table[i] = a        
        i += 1
    
    return table


def splitter(str):
# input: a string str
# output: list of splitted strings
# e.g 'abc' -> [['a','b','c'], ['ab','c'], ['a','bc']]
    combinations = []
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        combinations.append([start, end])
        for split in splitter(end):
            result = [start]
            result.extend(split)
            combinations.append(result)
    return combinations


def isDecoded(li: [], table: {}):
# input: 1 list of strings & 1 dictionary of hashTable
# output: return True/False if possible to hash
    for e in li:
        if int(e) not in table.keys():
            return False
    return True 


def decode(li:[], table: {}):
# input: 1 list of strings & 1 dictionary of hashTable
# output: 1 string decodedMsg
    decodeMsg = ''
    for e in li:
        decodeMsg += table[int(e)]
    return decodeMsg


def decodeWays(msg):
# input: 1 string msg
# output: int counter i.e no. ways which msg can be decoded
    posibleMsgs = splitter(msg)
    privateKey = mapping()

    # init returned variables
    counter = 0
    decodedList = []

    for message in posibleMsgs:
        if(isDecoded(message, privateKey)):
            counter += 1
            decodedList.append(decode(message, privateKey))

    return counter, decodedList


def decodeWays_test(message):
    print(message, decodeWays(message))


if __name__ == "__main__":
    decodeWays_test('111')  # return 3
    decodeWays_test('1234') # return 3
    decodeWays_test('001')  # return 0