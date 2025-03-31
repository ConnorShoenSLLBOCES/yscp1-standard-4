'''
Question 3: Nested Age Check
Description: Write a program that checks a person’s age and prints a message. The program should have the following logic:

If the person is below 13, print "Child".
If the person is between 13 and 19, print "Teenager".
If the person is between 20 and 64, print "Adult".
If the person is 65 or older, print "Senior".
If the person’s age is 18 or 21, print "Young Adult".
'''

# This program will check age categories
# Add if-elif-else logic here with nested conditions
try:
    age = int(input("Enter your age: "))
except ValueError:
    print ("Please enter a whole number.")
if age < 13:
    print ("Child")
elif age >= 65:
    print ("Senior")
elif age >= 20:
    if age == 21:
        print ("Young Adult")
    else:
        print ("Adult")
elif age >= 13:
    if age == 18:
        print ("Young Adult")
    else:
        print ("Teenager")