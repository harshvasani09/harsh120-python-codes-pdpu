stack = []

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        val = input("Enter value to push: ")
        stack.append(val)
        print("Pushed:", val)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == '3':
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty.")
    elif choice == '4':
        print("Stack:", stack[::-1] if stack else "Empty")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
