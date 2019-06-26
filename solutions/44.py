# -------------------------------------
# Author: Tuan Nguyen
# Date: 20190626
#!solutions/44.py
# -------------------------------------
"""
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. 
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. 
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""

def merge(A, B):
# input: 2 sorted arrays of ints A & B
# output: sorted array C from A+B & no. inversions in C 'k_c'
    C = []  # init output sorted array from A & B
    k_c = 0 # init no. inversion in C
    i_a = 0 # pivot in A
    i_b = 0 # pivot in B
    # merge in mergeSort. 
    # modified to compute k_c: if A[i_a] > B[i_b], then all elements from i_a to end of array A are bigger than B[i_b]
    while (i_a < len(A)) and (i_b < len(B)):    
        if A[i_a] > B[i_b]:
            C.append(B[i_b])
            i_b += 1
            k_c += len(A) - i_a
        else:
            C.append(A[i_a])
            i_a += 1
    # copy the rest of other array when 1 array is completed
    while i_a < len(A):
        C.append(A[i_a])
        i_a += 1
    while i_b < len(B):
        C.append(B[i_b])
        i_b += 1
    return C, k_c


def inversion(arr):
# input: list 'arr' of ints
# output: sorted arr & number of inversions 'arr' has
# method: modified mergeSort ~> running time: O(n*logn)
    # trivial case
    if len(arr) < 2:
        return arr, 0
    # split & recursion
    sorted_lArr, k_l = inversion(arr[:int(len(arr) / 2)])
    sorted_rArr, k_r = inversion(arr[int(len(arr) / 2):])
    # combine
    sorted_arr, k_m = merge(sorted_lArr, sorted_rArr)
    k = k_l + k_r + k_m
    return sorted_arr, k


def inversion_test(arr):
    print(arr, "~> no. inversions:", inversion(arr)[1])


if __name__ == "__main__":
    inversion_test([1, 2, 3, 4, 5]) # return 0
    inversion_test([2, 4, 1, 3, 5]) # return 3
    inversion_test([5, 4, 3, 2, 1]) # return 10