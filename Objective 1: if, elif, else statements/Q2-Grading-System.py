'''
Question 2: Grading System
Description: Write a program that takes a student's score as input and assigns a grade based on the following criteria:

90 or above: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
'''

# This program will assign grades based on the score
try:
    score = float(input("Enter the student's score: "))
except ValueError:
    print ("Please enter a number.")
# Complete the if-elif-else logic to assign grades
if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
elif score < 60:
    print ("F")