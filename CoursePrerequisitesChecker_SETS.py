collage_name = "Texas Tech University"
print(f"Welcome to {collage_name} AI Course Prerequisites Checker!\n")
texas_tech_ai_prerequisites ={
    "Math", "Programming", "Data Structure", "Machine Learning", "Statistics", "Liniar Algebra" , " Artificial Inteligence"
}

student_courses = set(input("Enter your copleted courses(comma separated):").split(","))
student_courses = {course.strip() for course in student_courses}

if texas_tech_ai_prerequisites.issubset(student_courses):
    print(f"Confratulations! You meet the prerequesites for the Ai course at {collage_name}")

else:
    print(f"You do not meet the prerequisites for the AI course at {collage_name}!")
    print("You need to complete this courses first:")
    for course in texas_tech_ai_prerequisites - student_courses:
        print("-", course)