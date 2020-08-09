# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start >= target:
        mid = (start + target) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, target, mid - 1, end)
        else:
            return binary_search(arr, mid + 1, start, end)
    else:
        return - 1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
    # Your code here
