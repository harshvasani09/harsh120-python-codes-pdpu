with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        filtered_words = [word for word in words if word.lower() not in ['a', 'the', 'an']]
        outfile.write(" ".join(filtered_words) + "\n")
