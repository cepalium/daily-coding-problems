# -------------------------
# Author: Tuan Nguyen
# Date: 20190526
# %13.py
# -------------------------
"""
Given an integer k and a string s, 
find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
"""


def longestSubstring(s, k):
# input: str s & int k
# output: longest substring w/ k distinct characters
    longestSubstr = ''
    for i in range(len(s)-1):
        e = i + 1
        while e < len(s):
            if (len(set(s[i:e])) == k) and (len(s[i:e]) > len(longestSubstr)):
                longestSubstr = s[i:e]
            e += 1
                
    return longestSubstr


def longestSubstring_test(s, k):
    print(s, k, longestSubstring(s, k))


if __name__ == "__main__":
    longestSubstring_test("abcba", 2)   # return "bcb"