def check_three_and_two(arr):
    counts = {char: arr.count(char) for char in set(arr)}

    return sorted(counts.values()) == [2, 3]