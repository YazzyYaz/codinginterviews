import math

def flip(arr, k):
    new_arr = arr[:k+1]
    if len(new_arr) > 1:
        new_arr = list(reversed(new_arr))
    final_arr = new_arr + arr[k+1:]
    return final_arr

def max_value(arr):
    n = 0
    for x in arr:
        if x > n:
            n = x
    return n

def pancake_sort(arr):
    for i in range(len(arr), 1, -1):
        val_max = max_value(arr[:i])
        max_index = arr.index(val_max)
        arr = flip(arr, max_index)
        arr = flip(arr, i-1)
    return arr

#arr = [1, 3, 2]
#arr = [1, 3, 1]
arr = [0, 1]
print(pancake_sort(arr))
