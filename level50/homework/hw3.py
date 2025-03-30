def reverse_words(input_string):
    words = input_string.strip().split()
    return ' '.join(words[::-1])