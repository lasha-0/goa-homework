def add_length(input_string):
    return [f"{word} {len(word)}" for word in input_string.split()]