#python weight converter
Weight = float(input("Enter Your Weight: "))
unit =input("kilograms or pounds?(K or L): ")

if unit == "K":
    Weight = Weight * 2.205
    unit ="lbs."
    print(f"Your Weight is : {round(Weight, 1)} {unit}")
elif unit == "L":
    Weight = Weight / 2.205
    unit = "Kgs."
    print(f"Your Weight is : {round(Weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")
