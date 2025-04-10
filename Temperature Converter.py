# Simple Python temperature converter

unit = input("Is the Temperature in celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature : "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is : {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in  celsius  is : {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")