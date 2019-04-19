# ITERATIVE BINARY SEARCH
# considered edge cases: 1. input value doesn't exist in the array, 2. empty array,
in_value = int(input())
_ = input()
in_array = [int(i) for i in input().split()]
def binary_search(value, array):
    low, high = 0, len(array)-1
    while low <= high:
        mid = low + (high - low) // 2
        mid_value = array[mid]
        if mid_value == value:
            return mid
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search(in_value, in_array))

# RECURSIVE BINARY SEARCH
# considered edge cases: 1. input value doesn't exist in the array, 2. empty array,
in_value = int(input())
_ = input()
in_array = [int(i) for i in input().split()]
def binary_search(value, array):
    if len(array) < 1:
        return -1
    return binary_search_helper(value, array, 0, len(array)-1)

def binary_search_helper(value, array, low, high):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    mid_value = array[mid]
    if mid_value == value:
        return mid
    elif mid_value < value:
        return binary_search_helper(value, array, mid + 1, high)
    else:
        return binary_search_helper(value, array, low, mid - 1)
    
print(binary_search(in_value, in_array))
