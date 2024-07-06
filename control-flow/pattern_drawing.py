while True:
    size = input("Enter the size of the pattern: ")
    if not size.isdigit() or int(size) <= 0:
        print("Please enter a positive integer.")
        continue
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()
    break    
