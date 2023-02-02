# if your guess number is 9, you win
import random
import random

# secret_number = 9
# guess_count = 0
# guess_limit = 5
# while guess_count < guess_limit:
#    user_guess = int(input("Guess : "))
#   guess_count = guess_count + 1
#    if user_guess == secret_number:
#       print("You win")
#       break
# else:
#    print("Try again")
# print("Done")

# for while loop
# initialize/assign  the factor
# state the condition
# increase or decrease the factor



print("""######################## Welcome to FAST and CURIOUS ######################################
        To Play, Select Start, To stop, Select Stop and to quit the came, select quit
        Enjoy the game !!!!!!!!!!!!!!!!!**************************************************
""")
controls = ""
started = False
stopped = False
while True:
    controls = input("> ").lower()
    if controls == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Ready to go ....")
    elif controls == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif controls == "help":
        print("""
    start - start the car
    stop - stop the car
    quit - quit the game
    help - displays help
    """)
    elif controls == "quit":
        break
    else:
        print("sorry I dont understand")
