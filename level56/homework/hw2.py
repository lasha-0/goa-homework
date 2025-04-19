import math

def find_next_square(sq):
    root = math.isqrt(sq)
    if root * root == sq:
        next_root = root + 1
        return next_root * next_root
    return -1