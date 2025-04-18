price = {
    "rice": 60,   
    "dal": 90,    
    "oil": 150    
qty = {
    "rice": 2,    
    "dal": 1,     
    "oil": 1      
}

total = 0

for item in qty:
    total += price.get(item, 0) * qty[item]

print("🧾 Total Bill Amount: ₹", total)
