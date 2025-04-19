def tail_swap(strings):
    first_left, first_right = strings[0].split(':')
    second_left, second_right = strings[1].split(':')
    return [f"{first_left}:{second_right}", f"{second_left}:{first_right}"]