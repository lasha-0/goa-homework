def find_odd(arr):
    result = 0
    for num in arr:
        result ^= num
    return result