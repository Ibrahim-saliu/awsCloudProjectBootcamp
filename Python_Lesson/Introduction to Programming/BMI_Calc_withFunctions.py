# This an app that calculate the BMI either using the imperial or the metric system.
# What will we need
# 	- weight in imperial units
# 	- weight in metric units
# 	- height in imperial units
# 	- height in metric units
# 	- formular for calculating BMI

def bmi_Calc():
    print("########################### Welcome to the Simple Universal BMI Calculator ############################## ")
    print("Please choose a calculation method. Make sure to choose any of the following options \n")
    print("where 1 is imperial \n"
          "  and 2 is metric \n"
          ""
          "Type either 1 or 2: \n")

    user_reply = int(input())
    if user_reply == 1:
        imperial_weight = float(input("Please enter you weight in metrics in pounds (lbs) : \n"))
        if not type(imperial_weight) == float:
            float(imperial_weight)
            print(f"You have entered {imperial_weight} lbs")

        imperial_height = float(input("Please enter your height in metrics in inches : \n"))
        if type(imperial_height) != float:
            float(imperial_height)
            print(f"You have entered {imperial_height} inches")
        bmi_imperial = (imperial_weight / (imperial_height * imperial_height)) * 703  # 703 is the conversion factor #
        print(f" Your BMI is {bmi_imperial} ")

        print("######################## Thank you for using the Simple Universal BMI Calculator #################")

    elif user_reply == 2:
        metric_weight = float(input("Please enter you weight in metrics in kilogram : \n"))
        print(f"You have entered {metric_weight} kg")
        if not type(metric_weight) == float:
            float(metric_weight)

        metric_height = float(input("Please enter your weight in metrics in cm : \n"))
        if not type(metric_height) == float:
            float(metric_height)
        convert_metric_height_to_meter = metric_height / 100
        print(f"You have entered {metric_height} cm which has been converted to {convert_metric_height_to_meter} m2")
        bmi_metric = metric_weight / (convert_metric_height_to_meter * convert_metric_height_to_meter)
        print(f" Your BMI is {bmi_metric} ")
        data_type = type(bmi_metric)

        print("######################## Thank you for using the Simple Universal BMI Calculator #################")

    else:
        print("You have not entered a valid entry!!! Please, enter a valida entry")


bmi_Calc()
