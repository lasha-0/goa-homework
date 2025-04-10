def remove_consecutive_duplicates(s):
    
    
    words = s.split()
    
    result = []
    
    for index in range(len(words)):
    
        current_word = words[index]
        previous = words[index - 1]
        
        if index == 0 or current_word != previous:
            result.append(current_word)
            
    return " ".join(result)