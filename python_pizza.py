print("Thank you for choosing Python Pizza Deliveries!")
size = input("What Size of Pizza do you want? S, M or L? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N? ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N? ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
else:
  print("Please choose a pizza size.")

print(f"Your final bill is: ${bill}.")
