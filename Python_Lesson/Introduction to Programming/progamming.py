print("Hello World!")
# Data Types ######
# strings, float, integer #

print(20 * 24 * 60)

# string concatenation - adding strings together using + sign #
print("There are " + str(24) + " hours in a day")
print(f"There are {24} hours in a day")
print(f"There are {2 * 3 * 4} hours in a day")
# f stands for format #

# Variables #
calculation_To_minutes = 24 * 60  # make the name of your variable very descriptive #
name_of_unit = "minutes" # name_of_unit is a global scope variable and can be used in other programmes and functions
print(f"There are {22 * calculation_To_minutes} {name_of_unit}")
print(f"There are {23 * calculation_To_minutes} {name_of_unit}")
print(f"There are {24 * calculation_To_minutes} {name_of_unit}")
print(f"There are {25 * calculation_To_minutes} {name_of_unit}")

# Functions - To avoid duplication of a piece of code #
# (blocks of code that deos something more complex #
# and used in case of avoiding the same logic in your code) #


def hours_in_a_day():
    print(f"There are {22 * calculation_To_minutes} {name_of_unit}")
    print(f"All good")


hours_in_a_day()


# Function Parameters - writing the function to use an argument#

def days_to_minutes(num_of_minutes, custom_message): # custom_message and num_of_minutes are local scope variable #
    return f"There are {num_of_minutes * calculation_To_minutes} {name_of_unit} in {num_of_minutes} days"

# we can create a variable in a function as well #


days_to_minutes(25, "All good")
days_to_minutes(100, "Yes sir")


# Accepting User Input #
user_input = input("Enter a number of days and I will convert it to input : \n  ")
user_input_number = int(user_input)  # This is called Casting  - converting string to an integer#
print(f"The user input given is {user_input}")

# Functions returning value #


def return_days_to_minutes(num_of_minutes): # custom_message and num_of_minutes are local scope variable #
    return f"There are {num_of_minutes * calculation_To_minutes} {name_of_unit} in {num_of_minutes} days"


return_var = return_days_to_minutes(100)
print(return_var)

user_input = input("Hey User, enter a number of days and I will convert it to input : \n  ")
calculated_value = return_days_to_minutes(user_input_number)
print(f"{calculated_value}")


