from _datetime import datetime

# prompting user for their gaol and deadline date
user_goal = input("Enter your goal with a deadline separated by a colon : \n")
user_goal_list = user_goal.split(":")
goal = user_goal_list[0]
deadline = user_goal_list[1]
print(user_goal_list)
print(deadline)

# we need the deadline as a date
deadline_date = (datetime.strptime(deadline, " " "%d.%m.%Y"))
# How many days from now till deadline
today_date = (datetime.today())
date_difference = (deadline_date - today_date)
print(f"Dear User!, the time left to reach your deadline is {date_difference.days} days")

