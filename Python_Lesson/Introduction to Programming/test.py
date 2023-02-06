
user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter a number of days and the conversion units : \n  ")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_unit_dict)
    print(days_unit_dict["days"])

