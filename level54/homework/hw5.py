def collatz(n):
    sequence = [str(n)]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(str(n))
    return "->".join(sequence)