def frequency(s):
    words = s.split()
    
    word_freq = {}
    
    for word in words:
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return dict(sorted(word_freq.items()))

test_string = "The quick brown fox jumps over the lazy dog the fox"
result = frequency(test_string)

print("Word Frequencies:", result)
