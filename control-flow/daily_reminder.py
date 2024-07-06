task = input("Enter your task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes/no)? ").lower()

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