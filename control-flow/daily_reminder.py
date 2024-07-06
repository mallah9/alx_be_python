task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

Reminder = f"Don't forget about your {priority} priority task: {task}"

if time_bound == "yes":
    Reminder += " that requires immediate attention today!"

match priority:
    case "high":
      print(f"** {Reminder} **")
    case "medium":
      print(Reminder)
    case "low":
      print(f"{Reminder} (optional)")
    case _:
      print("Invalid priority level. Reminder set with default priority.")
      print(Reminder)