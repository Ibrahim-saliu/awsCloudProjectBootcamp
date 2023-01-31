# LIST and FOR LOOP #

calculation_To_minutes = 24 * 60  # make the name of your variable very descriptive #
name_of_unit = "minutes"  # name_of_unit is a global scope variable and can be used in other programmes and functions


def return_days_to_minutes(num_of_minutes):  # custom_message and num_of_minutes are local scope variable #
    print(num_of_minutes > 0)  # this will print true if the condition is true
    if num_of_minutes > 0:
        return f"There are {num_of_minutes * calculation_To_minutes} {name_of_unit} in {num_of_minutes} days"
    elif num_of_minutes == 0:  # you can have multiple elifs in a conditional statement #
        return "You have entered zero, please enter a valid number"


def validate_and_executes():
    try:
        user_input_number = int(no_of_days)  # This is called Casting  - converting string to an integer#
        if user_input_number > 0:
            calculated_value = return_days_to_minutes(user_input_number)
            print(f"{calculated_value}")
        elif user_input_number == 0:  # you can have multiple elifs in a conditional statement #
            print("You have entered zero, please enter a valid number")
        else:
            print("But why have you entered a negative number, kindly enter a valid entry")
        # the block of code above calling the isdigit function will check if the user input is an integer #
    except ValueError:
        print("You have not entered a valid entry, please, do not ruin my program")


user_input = ""
while user_input != str("exit"):
    user_input = input("Hey User, enter number of days as comma-separated value and I will convert it to input : \n  ")
    print(type(user_input.split(",")))  # this print the types as list
    print(user_input.split(","))
    user_input_list = user_input.split(",")  # we save our list in a variable
    print(f" The first value in the list is : {user_input_list[0]}")
    user_input_list.append(100)  # we can add new items to the list
    print(user_input_list)
    for no_of_days in user_input.split(","):  # split function will return/convert into a list of value
        validate_and_executes()
