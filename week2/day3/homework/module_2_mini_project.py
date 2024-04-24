# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# ```
# Welcome to the To-Do List App!
    # Menu:
    # 1. Add a task
    # 2. View tasks
    # 3. Mark a task as complete
    # 4. Delete a task
    # 5. Quit

# #     ```

# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task (by default “Incomplete”).
# View the list of tasks
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete"). (BONUS)
# Deleting a task.
# Quitting the application.
# Marking a task as complete. 

todo_list = []
todo_status = []


while True:
    try:
        print('''
              Welcome to the To-Do List App!

                Menu:
                1. Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task5
                5. Quit
              ''')
        user_choice = int(input("Please enter your choice: "))
        if user_choice > 0 and user_choice <= 5:
            pass
        elif user_choice <= 0:
            raise ValueError("No Negative")
        elif user_choice > 5:
            raise ValueError("Greater")
    except ValueError as ve:
        if "No Negative" in str(ve):
            print("No Negative Values input allowed. Please try again")
        elif "Greater" in str(ve):
            print("Invalid input. Please enter your choice between 1 and 5")
        elif "Not Found" in str(ve):
            print("This task is not in your list. Please try again")
        else:
            print("Invalid input. Please enter your choice in numeric form between 1 and 5")
    else:
        try:
            if user_choice == 1:
                new_task = input("Please end the new task: ").capitalize()
                todo_list.append(new_task)
                todo_status.append("Incomplete")
            elif user_choice == 2:
                i = 0
                # print("\tTask\t|\tStatus")
                for todo in todo_list:
                    n = i+1
                    print(f"{n}.{todo}\t:\t{todo_status[i] if todo_status[i] == "Complete" else todo_status[i]}")
                    i += 1
            elif user_choice == 3:
                task_complete_choice = input("Please enter the task you want to mark complete: ").capitalize()
                i = 0
                b = 0
                for todo in todo_list:
                    if todo == task_complete_choice:
                        todo_status[i] = "\033[41mComplete\033[0m"
                    i += 1
                    b += 1
                if b == 0:
                    raise ValueError("Not Found")
            elif user_choice == 4:
                task_delete_choice = input("Please enter the task to delete from the list: ").capitalize()
                i = 0
                b = 0
                for todo in todo_list:
                    if todo == task_delete_choice:
                        todo_list.remove(task_delete_choice)
                        todo_status.pop(i)
                        b += 1
                    i =+ 1
                if b == 0:
                    raise ValueError("Not Found")
            elif user_choice == 5:
                print("\nThank you for using the To-Do List App.")
                print("\n")
                break
        except ValueError as nf:
                if "Not Found" in str(nf):
                    print("\nThis Task is not in your To-Do List. Please Try Again")
    finally:
        # print("Have a good Day. Hope you enjoyed!")
        pass