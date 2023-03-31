l_name = input("Enter student last name: ")
f_name = input("Enter student first name: ")
gpa= float(input("Enter your student GPA: "))

while True:
    if l_name== "ZZZ":
        break
    if gpa >= 3.5:
        print (" the student has made the Dean's List.")
        break
    elif gpa >= 3.25:
        print (" the studnet has made the Honor Roll.")
    else:
        print("Sorry the student nor either in Dean's list or Honer Roll.")
