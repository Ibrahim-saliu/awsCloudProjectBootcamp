# if-else statement #

# The application program below converts number of days into minutes #

calculation_To_minutes = 24 * 60  # make the name of your variable very descriptive #
name_of_unit = "minutes"  # name_of_unit is a global scope variable and can be used in other programmes and functions


def return_days_to_minutes(num_of_minutes):  # custom_message and num_of_minutes are local scope variable #
    print(num_of_minutes > 0)  # this will print true if the condition is true
    if num_of_minutes > 0:
        return f"There are {num_of_minutes * calculation_To_minutes} {name_of_unit} in {num_of_minutes} days"
    elif num_of_minutes == 0:  # you can have multiple elifs in a conditional statement #
        return "You have entered zero, please enter a valid number"


# the way this application is written has made provision for not letting a bad value crash the program #
# the isdigit function added also filters any float or negative number added #
# as a result, we do not need to add an else statement in the definition of our return_days_to_minutes function #

# To clean up our code, the user_input section will be embedded in a function called validate_and_execute

def validate_and_executes():
    if user_input.isdigit():
        user_input_number = int(user_input)  # This is called Casting  - converting string to an integer#
        calculated_value = return_days_to_minutes(user_input_number)
        print(f"{calculated_value}")
        # the block of code above calling the isdigit function will check if the user input is an integer #
    else:
        print("You have not entered a valid entry, please, do not ruin my program")


user_input = input("Hey User, enter a number of days and I will convert it to input : \n  ")
# user_input is a global variable so our functions have access to it #

validate_and_executes()

# if else can also be nested #
