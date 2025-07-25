# Student Marks Report Generator

# Input Section
student_name = input("Enter Student Name: ")

python_marks = int(input("Enter Python Marks   : "))
sql_marks = int(input("Enter SQL Marks      : "))
powerbi_marks = int(input("Enter PowerBI Marks  : "))

# Calculations
total = python_marks + sql_marks + powerbi_marks
average = total / 3

is_pass = python_marks >= 40 and sql_marks >= 40 and powerbi_marks >= 40

# Grade Assignment
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

# Report Output
print("\n------------------ STUDENT REPORT ------------------")
print(f"Name                : {student_name}")
print(f"Python              : {python_marks}")
print(f"SQL                 : {sql_marks}")
print(f"PowerBI             : {powerbi_marks}")
print(f"Total               : {total}")
print(f"Average             : {average:.2f}")
print(f"Result              : {'Pass' if is_pass else 'Fail'}")
print(f"Grade               : {grade}")
print("----------------------------------------------------")
