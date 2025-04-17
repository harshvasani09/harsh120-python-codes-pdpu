user_input = input("Please enter a string: ")

alphabet_count = 0
digit_count = 0
other_count = 0  

for character in user_input:
    if character.isalpha():
        alphabet_count += 1  
    elif character.isdigit():
        digit_count += 1     
    else:
        other_count += 1     

print("\nAnalysis of your input:")
print(f"Alphabets: {alphabet_count}")
print(f"Digits: {digit_count}")
print(f"Other characters: {other_count}")
