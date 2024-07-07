while True:
    print("\nShopping List Manager:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      item = input("Enter item name: ")
      shopping_list.append(item)
      print(f"{item} added to the list!")
    elif choice == '2':
      item = input("Enter item name to remove: ")
      if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list!")
      else:
        print(f"{item} not found in the list.")
    elif choice == '3':
      if shopping_list:
        print("Your Shopping List:")
        for item in shopping_list:
          print(f"- {item}")
      else:
        print("The shopping list is empty.")
    elif choice == '4':
      print("Exiting Shopping List Manager.")
      break
