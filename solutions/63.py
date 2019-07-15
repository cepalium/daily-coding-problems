# --------------------------------
# Author: Tuan Nguye
# Date: 20190715
#!solutions/63.py
# --------------------------------
"""
Given a 2D matrix of characters and a target word, 
write a function that returns whether the word can be found in the matrix 
by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', 
you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', 
you should return true, since it's the last row.
"""

def is_word_found(matrix, target):
# input: 2D matrix of characters 'matrix' & target word string 'target'
# output: True/False if target is found in matrix by going left->right, up->down
    # init var
    no_rows = len(matrix)
    no_cols = len(matrix[0])
    first_target_char = target[0]
    len_target = len(target)
    # loop in all matrix
    for i in range(no_rows):
        for j in range(no_cols):
            if matrix[i][j] == first_target_char:   # find the char in matrix matching with first target char
                row_string = ''.join(matrix[i][j:]) # string from that char till end of that row
                col_string = ''.join([row[j] for row in matrix[i:]])    # string from that char till end of that column
                if (len(row_string) >= len_target) and (row_string[:len_target] == target): # sucessfully find target in the row
                    return True
                if (len(col_string) >= len_target) and (col_string[:len_target] == target): # successfully find target in the column
                    return True
    return False    # no target in matrix


def is_word_found_test(matrix, target):
    for row in matrix:
        print(row)
    print('target:', target, '~>', is_word_found(matrix, target))


if __name__ == "__main__":
    is_word_found_test(matrix=[['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']],
                        target='FOAM')  # return True
    is_word_found_test(matrix=[['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']],
                        target='MASS')  # return True
    is_word_found_test(matrix=[['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']],
                        target='BS')  # return True
    is_word_found_test(matrix=[['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']],
                        target='ABCXYZ')  # return FALSE