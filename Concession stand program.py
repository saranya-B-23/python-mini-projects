# Concession stand program

menu = {"pizza": 3.00,
        "burger": 2.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "soda": 3.50,
        "lemonade": 4.25,
        "juices": 5.00}

cart = [] # keep track of the user selected items
total = 0

"""
:10 means:
➤ reserve 10 character spaces for this word.
➤ if the word is shorter than 10 characters, it adds spaces to the right.
.2f means:
➤ format the number as a floating-point number with 2 decimal places (e.g., 3.0 becomes 3.00).
"""
print("---------- MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------")

while True:
        food = input("Select an item from menu (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None: # menu.get(food)--------- Look in the menu and get the price of whatever the user typed (food)
                cart.append(food)

for food in cart:
        total += menu.get(food)
        print(food, end="  ")
print()
print(f"Total is: ${total :.2f}")
