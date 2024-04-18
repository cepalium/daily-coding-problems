# ----------------------------------
# Author: Tuan Nguyen
# Date created: 20200524
#!375.py
# ----------------------------------
"""
The h-index is a metric used to measure the impact 
and productivity of a scientist or researcher.

A scientist has index h if h of their N papers have at least h citations each, 
and the other N - h papers have no more than h citations each. 
If there are multiple possible values for h, the maximum value is used.

Given an array of natural numbers, 
with each value representing the number of citations of a researcher's paper, 
return the h-index of that researcher.

For example, if the array was:

[4, 0, 0, 2, 3]

This means the researcher has 5 papers with 4, 1, 0, 2, 
and 3 citations respectively. 
The h-index for this researcher is 2, since they have 
2 papers with at least 2 citations and the remaining 
3 papers have no more than 2 citations.
"""


def h_index(papers):
    N = len(papers)
    papers = sorted(papers, reverse=True)
    for i, num_citations in enumerate(papers):
        if i + 1 >= num_citations:  # at least h papers have h citations
            return num_citations
    return 0


def test1():
    assert h_index([4, 0, 0, 2, 3]) == 2


if __name__ == "__main__":
    test1()
