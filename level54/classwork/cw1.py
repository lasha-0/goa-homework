def vaporcode(s):
    result = ""
    s = s.replace(" ", "")
    for char in s:
        result += char.upper() + "  "
    return result[:-2]