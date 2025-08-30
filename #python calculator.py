#python calculator

operator = input("Enter an Operator(+ - * / %): ")
num1  = float(input(f"Enter the 1st Number: "))
num2  = float(input(f"Enter the 2nd Number: "))

if operator == "+":
  result = num1 + num2
  print(round(result, 3))
elif operator == "-":
  result = num1 - num2
  print(round(result, 3))
elif operator == "/":
  result = num1 / num2
  print(round(result, 3))
elif operator == "*":
  result = num1 * num2
  print(round(result, 3))
elif operator == "%":
  numb1 = float(input(f"Enter the scored number: "))
  numb2 = float(input(f"Enter the total number: "))
  result = (numb1/numb2)*100
  print(round(result, 3))
else:
  print(f"{operator} is not valid")