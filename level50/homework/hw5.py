def move_zeros(input_array):
    result = [x for x in input_array if x != 0]

    zero_count = input_array.count(0)

    result.extend([0] * zero_count)
    
    return result