names_set = set()

names_set.add("Amit")
names_set.add("Neha")
names_set.add("Ravi")
names_set.add("Priya")
names_set.add("Karan")

names_set.discard("Ravi") 
names_set.add("Vikas")     

names_set.discard("Neha")
names_set.discard("Priya")

print("Final set of names:", names_set)
