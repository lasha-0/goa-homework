def find_minimum(lst):
    min_value = lst[0]
    
    for num in lst:
        if num < min_value:
            min_value = num
    
    return min_value


numbers = [1, 546, 456, 123]
print(find_minimum(numbers))