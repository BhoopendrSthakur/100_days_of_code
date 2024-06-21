print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() 
extra_cheese = input() 
if size == "S":
  price = 15
  if add_pepperoni == "Y":
    price = price + 2
  else:
    price = price
elif size == "M":
  price = 20
  if add_pepperoni == "Y":
    price = price +3
  else:
    price = price
else:
  price = "25"
  if add_pepperoni == "Y":
    price = price +3
  else:
    price = price
if extra_cheese == "Y":
  price = price + 1
else:
  price = price

print("Thank you for choosing Python Pizza Deliveries!")
print(f"your final price is {price}")