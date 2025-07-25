# Welcome Message and Name Input 
print("Welcome to Mini Mart!")
user_name = input("Enter your name : ")

#Store items in dictionary (Data Type:dict)
items = {
    "apple" : 30,
    "banana": 10,
    "milk":50,
    "bread":40,
    "eggs":6
}

# Print available items using loop (Dict + String formatting)
print("\nAvailable Items : ")
for item , price in items.items():
    print(f"{item.title()} - ${price} per unit ")


# Take number of items to buy 
num_items = int(input("\n How many different items would you like to buy ?"))

# Initialize cart and total 
cart = {}
total = 0

# Loop to take item name and quantity 
for i in range(num_items):
    item_name = input(f"\nEnter item {i+1} name: ").lower()
    quantity = int(input(f"Enter quantity of {item_name}: "))

# check if item exits 
if item_name in items:
    price = items[item_name]
    subtotal = price * quantity
    cart[item_name]=(quantity,subtotal) 
    total+= subtotal

else:
    print("item not found. skipping....") 

# add tax and calculate grand total (operators)  
tax = total * 0.05 
grand_total = total + tax

#display final bill 
print("\n ---Final Bill ---")
print(f"customer : {user_name}")

for item , (qty ,subtotal) in cart.items():
    print(f"{item.title()} x {qty} = ${subtotal}")

print(f"subtotal: ${total}")
print(f"Tax (5%): ${tax:.2f}")
print(f"grand Total: ${grand_total: . 2f}")
print("------------------------")    
        