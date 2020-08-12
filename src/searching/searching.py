# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

	if start <= end:

		mid = (start + end) // 2

		if arr[mid] == target:
			return mid

		elif arr[mid] > target:

			return binary_search(arr, target, start, mid - 1)

		else:
			return binary_search(arr, target, mid+ 1, end)
	else:

		return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
	
	start = 0
	end = len(arr) - 1

	if start != end:

		mid = (start + end) // 2

		if arr[mid] == target:
			return mid

		elif arr[mid] > target:

			if arr[start] < arr[mid]:

				return agnostic_binary_search(arr[start:(mid - 1)], target)

			else:
				return agnostic_binary_search(arr, target, mid + 1, start)

		else:
			if arr[end] > arr[start]:

				return agnostic_binary_search(arr, target, mid+ 1, end)

			else:

				return agnostic_binary_search(arr, target, end, mid-1)


	else:

		return -1
