queue = []

while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue (Add)")
    print("2. Dequeue (Remove)")
    print("3. Peek (Front element)")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        item = input("Enter value to add to the queue: ")
        queue.append(item)
        print(f"'{item}' has been added to the queue.")
    elif choice == '2':
        if queue:
            removed = queue.pop(0)
            print(f"Removed from queue: {removed}")
        else:
            print("Queue is empty. Nothing to remove.")
    elif choice == '3':
        if queue:
            print("Front of the queue:", queue[0])
        else:
            print("Queue is empty.")
    elif choice == '4':
        print("Current queue:", queue if queue else "Queue is empty.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
