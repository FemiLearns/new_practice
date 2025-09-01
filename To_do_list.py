from functions import *

tasks=[]




while True:
    print("Welcome to the most reliable to do list")
    print("1. To add task\n2. To remove task\n3. To view task\n4. To exit the program")
    # Asking for input    
    try:
        choice = int(input("Enter your desired option:"))
    except:
        print("Enter a positive integer") 


    if choice == 1:
        while True:
            task = input("Please enter your task: ")
            add_task(task)
            print(f"'{task}' has been added")
            done = input("Type done if you are done adding taskK").lower()
            if done == "done":
                break
    elif choice == 2:
        task = input("please enter the task to remove")
        remove_task(task)
        print("These task has been removed from the task list")
    elif choice == 3:
        view_task()
        print(f"These are your task:\n")
    elif choice == 4:
        print("Good bye")
        break
    else:
        print("please enter a valid option")