#calculam prezenta

total_classes = int(input("Enter the total number of classes : "))
attended_classes = int(input("Enter the total number of classes you atteded : "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input. Please check the number you entered")

attended_percentage = (attended_classes/total_classes)*100

status = "Allowed to enter exam " if attended_percentage >= 75 else "Not allow to attend exam! "
message = "keep up the good work " if attended_percentage >= 75 else " Please improve your attendence!"

if total_classes > 0 and attended_classes >= 0 and attended_classes <= total_classes:
     print(f"Attendance : {attended_percentage:.2f} %")
     print(f"Status : {status}")
     print(f" Motivational message : {message}")