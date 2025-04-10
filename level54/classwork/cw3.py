def dna_to_rna(dna):
    rest = ""
    for i in dna:
        if i == "T":
            rest += "U"
        else:
            rest += i
    return rest