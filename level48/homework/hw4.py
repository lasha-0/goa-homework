def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = arr.count(0)
    return non_zeros + [0] * zeros