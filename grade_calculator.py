# Student Grade Calculator Program

# Taking student name as input
name = input("Enter student name: ")

# Taking marks for 3 subjects
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))

# Calculating total marks
total = m1 + m2 + m3

# Calculating average
average = total / 3

# Determining grade using if-elif-else
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'

# Displaying the result
print("\n----- RESULT -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)