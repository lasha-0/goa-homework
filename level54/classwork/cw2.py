def is_isogram(string):
    seen = []
    string = string.lower()
    for character in string:
        if character in seen:
            return False
        seen.append(character)
    return True