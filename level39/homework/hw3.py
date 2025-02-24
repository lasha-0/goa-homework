def digitize(n):
    def digitize(n):
        digits=[]
        n_str=str(n)
        for i in range(len(n_str)-1, -1, -1):
            digits.append(int(n_str[i]))
            return digits