from datetime import datetime

user_input = input(
    "enter your goal with a deadline separated by a colon (<goal>:<dd.mm.yyyy>): ")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

date = datetime.strptime(deadline, "%d.%m.%Y")
now = datetime.today()

time_til = date - now

print(f"Days remaining to your goal: {time_til.days}")
