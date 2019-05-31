# -------------------------
# Author: Tuan Nguyen
# Date: 20190531
#!solutions/18.py
# -------------------------
"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.
"""


# library
import collections


def slidingWindowMaximum(arr, k):
# input: list of ints arr & window-sized int k
# output: sliding window of size k maximum from arr 
# method: double-ended queue "deq"
	slidingWindowMax = []		# init returned list
	deq = collections.deque()	# init double-ended queue, store index
	# 1st window
	for i in range(k):
		# remove indexes of smaller values in 1st window if the later index comes a bigger value
		while deq and (arr[i] > arr[deq[0]]):		
			deq.pop()
		deq.append(i)	# add current-element index into deq
	# rest
	for i in range(k, len(arr)):
		slidingWindowMax.append(arr[deq[0]])	# add max value of previous window, aka index 0 in deq, into output
		# remove all previous indexes not in current window
		while deq and (deq[0] <= i-k):			
			deq.popleft()
		# remove all indexes of smaller values in current window
		while deq and (arr[i] > arr[deq[-1]]):	
			deq.pop()
		deq.append(i)							# add current-element index into deq
	slidingWindowMax.append(arr[deq[0]])		# add max value of last window into output
	return slidingWindowMax


def slidingWindowMaximum_test(arr, k):
	print(arr, k, slidingWindowMaximum(arr, k))


if __name__ == '__main__':
	slidingWindowMaximum_test([10, 5, 2, 7, 8, 7], 3)	# return [10, 7, 8, 8]
