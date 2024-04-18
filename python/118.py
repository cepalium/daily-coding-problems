# ---------------------------
# Author: Tuan Nguyen
# Date created: 20190910
#!solutions/118.py
# ---------------------------
"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def sortedSquareArray(array):
    # input: sorted list of integers
    # output: sorted list of square integers from input list
    # running time: O(n)
    output = []  # output array initialized
    # split into negative and positive arrays
    negativeArray = [i for i in array if i < 0]
    positiveArray = [i for i in array if i >= 0]
    # reverse negative array
    negativeArray = negativeArray[::-1]
    # square each element in both arrays
    negativeArray = [i * i for i in negativeArray]
    positiveArray = [i * i for i in positiveArray]
    # merge (like in merge sort)
    j_n = 0  # pivot of negative array
    j_p = 0  # pivot of positive array
    while j_n < len(negativeArray) and j_p < len(positiveArray):
        if (
            negativeArray[j_n] <= positiveArray[j_p]
        ):  # negative array has smaller element in current pivots
            output.append(negativeArray[j_n])  # add this element into output
            j_n += 1  # move pivot
        else:  # same for smaller element in positive array
            output.append(positiveArray[j_p])
            j_p += 1
    # copy the rest after fully merging 1 array
    while j_n < len(negativeArray):
        output.append(negativeArray[j_n])
        j_n += 1
    while j_p < len(negativeArray):
        output.append(positiveArray[j_p])
        j_p += 1
    return output


def sortedSquareArray_test(array):
    print(array, "~>", sortedSquareArray(array))


if __name__ == "__main__":
    sortedSquareArray_test([-9, -2, 0, 2, 3])  # return [0, 4, 4, 9, 81]
