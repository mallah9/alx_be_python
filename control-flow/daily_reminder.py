task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"Don't forget about your {priority} priority task: {task}"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

match priority:
    case "high":
      print(f"** {reminder} **")
    case "medium":
      print(reminder)
    case "low":
      print(f"{reminder} (optional)")
    case _:
      print("Invalid priority level. Reminder set with default priority.")
      print(reminder)