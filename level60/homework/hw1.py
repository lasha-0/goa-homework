def difference_of_squares(n):

    sum_of_numbers = sum(range(1, n + 1))

    square_of_sum = sum_of_numbers ** 2

    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))

    return square_of_sum - sum_of_squares
