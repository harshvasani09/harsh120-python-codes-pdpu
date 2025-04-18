def count_alpha_digits(s):
    alphabet_count = 0
    digit_count = 0
    
    for ch in s:
        if ch.isalpha():
            alphabet_count += 1
        elif ch.isdigit():
            digit_count += 1

    return {"alphabets": alphabet_count, "digits": digit_count}

sample_string = "Hello123, this is a test string with numbers 4567!"
result = count_alpha_digits(sample_string)

print("Count of Alphabets and Digits:", result)
