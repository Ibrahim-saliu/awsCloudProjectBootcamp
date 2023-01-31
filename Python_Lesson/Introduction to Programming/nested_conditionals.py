# if-else statement #

# The application program below converts number of days into minutes using nested conditional statement #

calculation_To_minutes = 24 * 60  # make the name of your variable very descriptive #
name_of_unit = "minutes"  # name_of_unit is a global scope variable and can be used in other programmes and functions


def return_days_to_minutes(num_of_minutes):  # custom_message and num_of_minutes are local scope variable #
    return f"There are {num_of_minutes * calculation_To_minutes} {name_of_unit} in {num_of_minutes} days"


# the section below shows the nesting # Though it is not recommended to have multiple nested conditionals #
def validate_and_executes():
    if user_input.isdigit():
        user_input_number = int(user_input)  # This is called Casting  - converting string to an integer#
        if user_input_number > 0:
            calculated_value = return_days_to_minutes(user_input_number)
            print(f"{calculated_value}")
        elif user_input_number == 0:  # you can have multiple elifs in a conditional statement #
            print("You have entered zero, please enter a valid number")
        # the block of code above calling the isdigit function will check if the user input is an integer #
    else:
        print("You have not entered a valid entry, please, do not ruin my program")


user_input = input("Hey User, enter a number of days and I will convert it to input : \n  ")
# user_input is a global variable so our functions have access to it #

validate_and_executes()


# if else can also be nested #
# To avoid Error, you can use the try/except command to try the execution of a code and capture the potential error #
# in other programming languages, it can be referred to as try/catch method #
# For example, the program above would look like this : #

def try_and_executes():
    try:
        user_input_number = int(user_input)  # This is called Casting  - converting string to an integer#
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


try_and_executes()
