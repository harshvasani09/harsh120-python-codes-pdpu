def ispangram(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

    input_set = set(s.lower())
    if alphabet_set <= input_set:
        return True
    else:
        return False
test_string1 = "The quick brown fox jumps over the lazy dog"
test_string2 = "Crazy Fredrick bought many very exquisite opal jewels"

print(f"Is the first sentence a pangram? {ispangram(test_string1)}")
print(f"Is the second sentence a pangram? {ispangram(test_string2)}")
