marks = {}

for i in range(5):
    subject = input("Enter your subject:\n")
    grade = int(input("Enter your grade:\n"))

    marks[subject]= grade

print(marks)
total_grades = sum(marks.values())
print(f"Your total grade is: {total_grades}")

average = total_grades/5
print(f"Your average is: {average}")
highest_grade = max(marks, key=marks.get)

print("{} is your best performing subject".format(highest_grade))