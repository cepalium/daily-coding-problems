# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200112
#!212.py
# ------------------------------
"""
Spreadsheets often use this alphabetical encoding for its columns: 
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 
For example, given 1, return "A". Given 27, return "AA".
"""
def alphabet_col_id(col_num):
    """ return alphabetical column id of a column number in spreadsheets """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    len_alphabet = len(alphabet)
    col_id = ""
    while col_num > 0:
        q = (col_num - 1) // len_alphabet
        r = (col_num - 1) % len_alphabet
        col_id = alphabet[r] + col_id
        col_num = q
    return col_id

def test_alphabet_col_id():
    assert alphabet_col_id(1) == "A"
    assert alphabet_col_id(27) == "AA"

if __name__ == "__main__":
    test_alphabet_col_id()