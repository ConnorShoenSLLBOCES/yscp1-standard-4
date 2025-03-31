'''
Question 1: Check for Even or Odd
Description: Write a program that takes an integer as input and checks if it's even or odd using a combination of relational and logical operators.
'''

# This program will check if the input number is even or odd

number = int(input("Enter a number: "))
# Use relational and logical operators to check for even/odd & Print out which it is to the terminal
e_or_o = number % 2
if e_or_o == 0:
    print (f"{number} = Even")
else:
    print (f"{number} = Odd")