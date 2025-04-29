def rotate_matrix_90_left(matrix):
    transposed = list(zip(*matrix))

    rotated = [list(row)[::-1] for row in transposed]
    
    return rotated