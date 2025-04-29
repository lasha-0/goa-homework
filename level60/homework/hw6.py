def count_consonants(text):
    vowels = 'aeiouAEIOU'
    
    consonant_count = 0
    
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    
    return consonant_count
