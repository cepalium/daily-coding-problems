# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200224
#!287.py
# ----------------------------
"""
You are given a list of (website, user) pairs that represent users visiting websites. 
Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
"""
import pandas as pd

def k_most_similar_pair_websites(pairs, k):
    """ return top k similar pair of websites based on visiting users """
    if k == 0:    # trivial case
        return []
    visit_matrix, websites, users = build_matrix(pairs)
    similarities = build_similarity_list(visit_matrix)
    top_k = [(similarities[i][0], similarities[i][1]) for i in range(k)]    # list of tuples (web_a, web_b) 
    return top_k

def build_matrix(pairs):
    """ return 2D matrix, column = websites, index = users """
    websites = set()
    users = set()
    for web, user in pairs:    # build list of distinct websites and users
        websites.add(web)
        users.add(user)
    websites, users = sorted(websites), sorted(users)    # sort websites & users
    visit_matrix = pd.DataFrame(0, columns=websites, index=users)    # visit_matrix is full of 0
    for web, user in pairs:    # fill visit of user to website to 1
        visit_matrix.at[user, web] = 1
    return visit_matrix, websites, users

def build_similarity_list(matrix):
    """ return descendingly-sorted list of (x, y, sim) which sim = similarity(x, y) from matrix """
    col = matrix.columns
    n = len(col)
    similarities = []
    for i in range(0, n-1):
        for j in range(i+1, n):
            sim = similarity(matrix[col[i]].to_numpy(), matrix[col[j]].to_numpy())
            similarities.append((col[i], col[j], sim))
    similarities = sorted(similarities, key=lambda similarities: similarities[2], reverse=True)
    return similarities

def similarity(A, B):
    """ return number of matching bits from 2 bit-array A & B """
    counter = 0
    n = len(A) if len(A) <= len(B) else len(B)    # max match number is the smaller length
    for i in range(n):
        if A[i] == B[i]:    # found a matching pair of bits
            counter += 1
    return counter

# ----- UNIT TEST -----
pairs = [('a', 1), ('a', 3), ('a', 5),
        ('b', 2), ('b', 6),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
        ('d', 4), ('d', 5), ('d', 6), ('d', 7),
        ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

def test1():
    assert k_most_similar_pair_websites(pairs=pairs, k=0) == []

def test2():
    assert k_most_similar_pair_websites(pairs=pairs, k=1) == [('a', 'e')]

def test3():
    assert k_most_similar_pair_websites(pairs=pairs, k=2) == [('a', 'e'), ('a', 'c')]

def test4():
    assert k_most_similar_pair_websites(pairs=pairs, k=3) == [('a', 'e'), ('a', 'c'), ('c', 'e')]


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()