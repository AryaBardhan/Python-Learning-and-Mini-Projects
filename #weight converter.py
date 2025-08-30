#weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds (K, L): ")

if unit == "K":
  weight = weight * 2.206
  unit = "Lbs."
  print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
  weight = weight / 2.206
  unit = "Kgs."
  print(f"Your weight is {round(weight, 1)} {unit}")
else:
  print(f"{unit} is not valid")



