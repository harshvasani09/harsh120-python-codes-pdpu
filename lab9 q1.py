def count_lower_upper(s):
    lower_count = 0
    upper_count = 0

    for ch in s:
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1

    return {"Lowercase": lower_count, "Uppercase": upper_count}

sample_string = "Hello World! How Are You?"
result = count_lower_upper(sample_string)

print("Count of Lowercase and Uppercase letters:", result)
