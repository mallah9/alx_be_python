def display_menu():
  """
  This function displays the menu options for the shopping list manager.
  """
  print("Shopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")

  item_name = input("Enter item name: ")
  return item_name

  item_name = get_item_name()
  shopping_list.append(item_name)
  print(f"{item_name} added to the list!")

  item_name = get_item_name()
  if item_name in shopping_list:
    shopping_list.remove(item_name)
    print(f"{item_name} removed from the list!")
  else:
    print(f"{item_name} not found in the list.")

  if shopping_list:
    print("Your Shopping List:")
    for item in shopping_list:
      print(f"- {item}")
  else:
    print("The shopping list is empty.")

  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      add_item(shopping_list)
    elif choice == '2':
      remove_item(shopping_list)
    elif choice == '3':
      view_list(shopping_list)
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")