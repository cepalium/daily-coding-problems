# ----------------------------
# Author: Tuan Nguyen
# Date created: 20200110
#!241.py
# ----------------------------
"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. 
If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. 
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""


def h_index(citations):
    """ """
    n = len(citations)
    citations = sorted(citations, reverse=True)  # decreasing-order citations
    h = 0  # result of h-index
    for i in range(n - 1, -1, -1):
        position = i + 1
        f = citations[i]
        if f <= position:  # look for the last position in which f >= position
            h = f
        else:
            break  # paper citations > paper order
    return h


def test_h_index():
    assert h_index([4, 3, 0, 1, 5]) == 3
    assert h_index([10, 8, 5, 4, 3]) == 4
    assert h_index([25, 8, 5, 3, 3]) == 3


if __name__ == "__main__":
    test_h_index()
