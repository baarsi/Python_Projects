todo_list = []

# Main loop to manage the to-do list
while True:
    if not todo_list:
        print("Your ToDo list is empty")
    else:
        index = 1
        for task in todo_list:
            print(f"{index}. {task}")
            index += 1

    # User options to add, remove tasks or quit
    print("Options:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Quit")
    choice = input()

    # Add a task to the to-do list
    if choice == "1":
        print("Adding task")
        new_task = input("Enter the task: ")
        todo_list.append(new_task)
    
    # Remove the last task from the list
    elif choice == "2":
        if not todo_list:
            print("Empty!")
        else:
            todo_list.pop()
    
    # Exit the loop and quit the application
    elif choice == "3":
        print("Quitting")
        break
