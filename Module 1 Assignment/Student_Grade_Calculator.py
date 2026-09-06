print("\n==Student Grade Calculator==\n")

x=False

while x==False:
    name=input("Enter Student Name: ")

    print("Enter the Marks,")
    bangla=int(input("Bangla: "))
    english=int(input("English: "))
    math=int(input("Math: "))

    total_marks=bangla+english+math
    avg_marks=total_marks/3

    grade=" "

    if avg_marks>=80:
        grade="A+"
    elif avg_marks>= 70 and avg_marks<80:
        grade="A"
    elif avg_marks>=60 and avg_marks<70:
        grade="B"
    elif avg_marks>=50 and avg_marks<60:
        grade="C"
    elif avg_marks<50:
        grade="F"
    else:
        grade="Something went wrong."

    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {avg_marks: .2f}")
    print(f"Grade: {grade}\n")

    temp=input("Exit (Y/N): ")
    print()

    if temp=="Y":
        x=True
    elif temp=="N":
        x=False
    else:
        print("Invalid Input.")