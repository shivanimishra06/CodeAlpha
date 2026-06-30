def todo_app():
    tasks = []

    print("----- WELCOME TO TO-DO LIST APP -----")

    total_task = int(input("Enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks:\n{tasks}")

    while True:
        print("\n--- MENU ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")

        operation = int(input("Choose operation: "))

        if operation == 1:
            new_task = input("Enter task to add: ")
            tasks.append(new_task)
            print("Task added successfully.")

        elif operation == 2:
            remove_task = input("Enter task to remove: ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif operation == 3:
            print("\nToday's tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

        elif operation == 4:
            update_task = input("Enter task to update: ")
            if update_task in tasks:
                new_task = input("Enter new task: ")
                index = tasks.index(update_task)
                tasks[index] = new_task
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif operation == 5:
            print("Exiting app...")
            break

        else:
            print("Invalid choice. Try again.")


todo_app()