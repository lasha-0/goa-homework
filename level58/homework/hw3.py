def capitalize(s):
    even_caps = ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(s))
    odd_caps  = ''.join(c.upper() if i % 2 == 1 else c for i, c in enumerate(s))
    return [even_caps, odd_caps]