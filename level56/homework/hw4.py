def double_every_second(lst):
    return [num * 2 if i % 2 == 1 else num for i, num in enumerate(lst)]