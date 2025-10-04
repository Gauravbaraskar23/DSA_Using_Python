def long_words(n , str):
    words_len = []
    txt = str.split(" ")
    
    for x in txt:
        if len(x) > n:
            words_len.append(x)
        
    return words_len

print(long_words(3 , "The quick brown fox jumps over the lazy dog"))