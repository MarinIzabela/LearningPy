
print("Welcome to the Daily Task Reminder : ")

input_tasks = int(input("Please enter the number of tasks"))

task_summary = "";
print("\n Enter your task and their deadline: ")
for task_number in range(1, input_tasks+1):
    task = input(f"Enter  task {task_number} : ")
    deadline = input(f" \nEnter the deadline for task {task} , ex: 5 PM => ")
    print(f"Reminder set! Complete {task} for {deadline} today !")
    task_summary+=f"task{task_number} : {task} (Deadline {deadline})\n"

print("\n All tasks have been enetered! ")
print("Stay productive and make sure to complete your tasks in time!\n\n !")
print(f"Summary of today's task and the deadline : \n {task_summary}")
print("Thank you for using Daily Task Reminder Program !")

