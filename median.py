"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas:  git ")
         print("Enter a list of numbers separated by commas:  git ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input-2 could not be converted to a number!")
    else:
        break
print(numbers)
