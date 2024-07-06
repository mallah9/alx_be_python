task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = f"{task} is a {priority} priority task "

if time_bound == "yes":
    reminder += "that requires immediate attention today!"

match priority:
    case "high":
      print(f"Reminder: {reminder} ")
    case "medium":
      print(f"Reminder: {reminder}")
    case "low":
      print(f"Reminder: {reminder} (optional)")
