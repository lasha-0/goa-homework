def find_uniq(arr):
    arr = [s.replace(" ", "").lower() for s in arr]

    from collections import Counter
    counter = Counter(arr)

    for string in arr:
        if counter[string] == 1:
            return arr[arr.index(string)].strip()