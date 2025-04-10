#simple python calculator
operator = input("Enter an operator(+,-,*,/):")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the first number:"))

if operator == "+":
   result = num1+num2
   print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))#round off result to 3 digits
else:
    print(f"{operator} is not valid ")