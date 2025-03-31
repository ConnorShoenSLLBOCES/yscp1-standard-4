'''
Question 3: Nested Loops (Multiplication Table)
Description: Write a program that uses nested loops to print the multiplication table for numbers 1 to 5.
'''

# This program will print the multiplication tables from 1 to 5 
# Use a for loop to iterate through the numbers for each table
for i in range(1,6):
    print (f"\nTable for {i}")
    # Use a nested loop to print the table for each number
    for f in range(1,6):
        table = i * f
        print (f" {i} * {f} = {table}")