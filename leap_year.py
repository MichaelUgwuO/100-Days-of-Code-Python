# Which year do you want to check?
year = int(input("Type the year: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It's a Leap year")
    else:
      print("It's Not leap year")
  else:
    print("It's a Leap year")
else:
  print("It's Not leap year")