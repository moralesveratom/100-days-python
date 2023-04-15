print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

pepperoni_small_pizza = 2
pepperoni_medium_large_pizza = 3
extra_cheese_any_pizza = 1

bill = 0

if size == "S":
    bill += small_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_small_pizza
    if extra_cheese == "Y":
        bill += extra_cheese_any_pizza

elif size == "M":
    bill += medium_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_pizza
    if extra_cheese == "Y":
        bill += extra_cheese_any_pizza

elif size == "L":
    bill += large_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_pizza
    if extra_cheese == "Y":
        bill += extra_cheese_any_pizza

print(f'Your final bill is: ${bill}.')
