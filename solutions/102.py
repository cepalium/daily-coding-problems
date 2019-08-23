# ----------------------------
# Author: Tuan Nguyen
# Date created: 20190823
#!solutions/102.py
# -----------------------------
"""
Given a list of integers and a number K, 
return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, 
then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def findContiguousSum(a, K, r):
# input: sorted array a of int & int K
# output: continuous sub-list of a s.t sum to K
    s = sum(a)
    # trivial case, then combine
    if (s == K) and (a not in r):
        r.append(a)
    # recursion
    if s - a[0] >= K:
        findContiguousSum(a[1:], K, r)
    if s - a[-1] >= K:
        findContiguousSum(a[:-1], K, r)


def contiguousList(a, K):
    result = []
    a = sorted(a)
    findContiguousSum(a, K, result)
    return result
    

def test(a, K):
    print(a, K, '~>', contiguousList(a, K))


if __name__ == "__main__":
    test(a=[1,2,3,4,5], K=9)    # return [[2,3,4], [4,5]]