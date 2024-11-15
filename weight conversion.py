weight= float(input("ENter weight: "))
unit= input("ENter unit K or L: ")
if unit=="k" or unit=="K":
    weight= weight*2.205
    unit= "LBS"
    print(f" your weight in {unit} is {weight} {unit}")
elif unit=="L" or unit=="l":
    weight= weight/2.205
    unit= "KGs"
    print(f" your weight in {unit} is {weight} {unit}")
else:
    print("Invalid unit")
