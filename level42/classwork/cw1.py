def replace_exclamation(st):
    answer=""
    for char in st:
        if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            char = "!"
        answer += char
    return answer