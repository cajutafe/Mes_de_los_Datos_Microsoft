# EXERCISES

# ----------------------------------------------------------------------

# Your first program
# You will use a Jupyter notebook to create your first program. Your senior officer wants you to create code to perform a couple of utilities. You will start by displaying today's date. Then you will add code to convert parsecs to lightyears.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

from datetime import date
print(date.today())

# Build a unit converter
# Now it's time to turn your attention to the second utility, converting parsecs to lightyears. One parsec is 3.26 lightyears, so you will multiply parsecs by that value to determine lightyears.

# Create a variable named parsecs and set it to 11. Then add the code to perform the appropriate calculation and store the result in a variable named lightyears. Finally print the result on the screen with so it displays a message which resembles the following:

# 11 parsecs is ___ lightyears

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


# Creating reusable applications
# Having a program with hard-coded values limits its flexibility. Your first officer likes the program you built to convert parsecs to lightyears, but wants the ability to specify a value for parsecs. She wants you to create a program which can accept user input.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

parsecs_input = input("number of parsecs ")
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


# ----------------------------------------------------------------------
# Exercise: Use logic to examine an object's size
# You will start your project by creating the code to determine if a piece of space debris is of a dangerous size. For this exercise we will use an arbitrary size of 5 meters cubed (5m3); anything larger is a potentially dangerous object.

# For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

# In the cell below, add a variable named object_size and set it to 10 to represent 10m3. Then add an if statement to test if object_size is greater than 5. If it is, display a message saying We need to keep an eye on this object. If it's less than 5, display a message saying Object poses no threat.

object_size = 10
if object_size > 5:
    print("We need to keep an eye on this object.")
else:
    print("Object poses no threat.")