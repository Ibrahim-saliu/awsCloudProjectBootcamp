# temperature = ["hot", "cold"]
# user_Entry = (input("What is the temperature of the day? "))
# print(type(user_Entry))
# if user_Entry == temperature[0]:
#    print(f"It is a {temperature[0]} day, so, drink a lot of water.")
# elif user_Entry == temperature[1]:
#     print(f"It is a {temperature[1]} day, so, wear some warm clothes.")
# else:
#    print("Please, enter a valid answer !!!")


weight = int(input("Weight : "))
unit = str(input("Unit : "))
kg = "kg"
lbs = "lbs"
weight_in_lbs = weight * 2.205
weight_in_kg = weight * 0.45

if unit.lower() == kg:
    print(f"You have entered your weight in kg")
    print(f"Your weight in pound is {weight_in_lbs}lbs")
elif unit.lower() == lbs:
    print(f"You have entered your weight in lbs")
    print(f"Your weight in kg is {weight_in_kg}kg")
else:
    print("Enter a valid unit")
