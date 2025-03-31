'''
Question 1: Weather Alert System

Description: Write a program that takes a temperature input from the user and prints whether the weather is hot, cold, or moderate. If the temperature is above 30°C, print "Hot". If it's below 10°C, print "Cold". Otherwise, print "Moderate". If the temperature is exactly 25°C, print "Perfect weather!".
'''

# This program will check the temperature and give a weather update
try:
    temperature = float(input("Enter the temperature in °C: "))
except ValueError:
    print ("Please enter a number.")
# Complete the if-elif-else logic here
if temperature > 30:
    print ("Hot")
elif temperature < 10:
    print ("Cold")
elif temperature == 25:
    print ("Perfect Weather!")
else:
    print ("Moderate")