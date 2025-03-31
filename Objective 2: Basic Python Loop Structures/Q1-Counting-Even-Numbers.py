'''
Question 1: Counting Even Numbers

Description: Write a program that counts how many even numbers there are in a list of numbers (from 1 to 20).
'''

# This program will count even numbers in a list
numbers = list(range(1, 21))
even_count = 0
# Loop through the numbers and check for even numbers
for i in numbers:
    e_or_o = i % 2
    if e_or_o == 0:
        print (f"{i} = Even")
    else:
        print (f"{i} = Odd")