# Student Grade Calculator

name = input("Enter student name: ")

m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print("\n----- RESULT -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)