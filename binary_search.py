import math

def binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while lo < hi:
        m = math.floor(lo + (hi-lo)/2)
        v = arr[m]

        if v == target:
            return True
        if v > target:
            hi = m
        else:
            lo = m +1

    return False

arr = [1,2,3,4,5,6,7,12,32,34,54,76,78,98]

res = binary_search(arr, 100)
print(res)
