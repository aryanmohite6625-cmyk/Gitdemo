Students_marks={"Alice":85,"Bryan":90,"Ryan":80,"Arisu":87}
name=input("Enter the name of the student: ")
if name in Students_marks:
    print(f"{name} have scored {Students_marks[name]} marks!")
else:
    print("Student not found!!.")