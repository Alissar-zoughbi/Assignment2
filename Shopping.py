
groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

cart = []

while True:
   
    item = input("What do you want to buy? ").lower()


    if item == "done":
        break

  
    if item in groceries:
        cart.append(item)
    else:

        print("Sorry, we don’t have that item.")

total = 0
for thing in cart:
    total += groceries[thing]  

print("\nYou bought:", cart)
print("Total = $", total)

