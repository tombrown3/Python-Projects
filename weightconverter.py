weight = int(input("Enter your weight :"))
unit = (input("Your weight is in (L) lbs or (K) Kilos :"))
print(unit)
if unit == 'k' or unit == 'K':
    weight = weight * 2.20 # conversion from kilos to lbs
    print(f"{weight} lbs is your weight converted from kilos")
elif unit == 'l' or unit == 'L':
    weight = weight * 0.45 # conversion from lbs to kilos
    print(f"{weight} kilos is your weight converted from lbs")    