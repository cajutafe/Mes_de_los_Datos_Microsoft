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


# ----------------------------------------------------------------------
# Exercise: Use complex logic to determine possible evasive maneuvers
# In the previous exercise you created code to test the size of the object. Now you will test both the object's size and proximity. You will use the same threshold for size of 5m3. If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

# For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

# Add the code to the cell below to create two variables: object_size and proximity. Set object_size to 10 to represent 10m3. Set proximity to 9000.

# Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5 and proximity is less than 1000. Otherwise display a message saying Object poses no threat.

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print("Evasive maneuvers required")
else:
    print("Object poses no threat")


# ----------------------------------------------------------------------
# Exercise: Transform strings

# There are several operations you can perform on strings when you manipulate them. In this exercise, you'll use string methods to modify text with facts about the Moon and then extract information to create a short summary.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# ## Parsing interesting facts about the moon

# Start by storing the following paragraph in a variable named `text`:

# ```
# Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.
# ```

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


# Separate the paragraph into sentences
# In English each sentence ends with a period. You will use this to break the paragraph into difference sentences. Using the split method to split the text into sentences by looking for the string . (a period followed by a space). Store the result in a variable named sentences. Print the result.

sentences = text.split('.')
print(sentences)


# Find keywords
# You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

# ----------------------------------------------------------------------

# Exercise: Formatting strings
# Knowing how to format strings is essential when you're presenting information from a program. There are a few different ways to accomplish this in Python. In this exercise, you use variables that hold key facts about gravity on various moons and then use them to format and print the information.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Create the variables
# Start by creating three variables, name, gravity, and planet, and set them to the following values:

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

# Create the template
# Now you will create the template to display the information about the moon. You want the output to look like the following:

# Gravity Facts about {name}
# --------------------------
# Planet Name: {planet}
# Gravity on {name}: {gravity} m/s2

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

# Use the template
# With the template created, it's time to use it to display information about the moon! Use the format function on template to use the template and print the information. Set name, planet, and gravity to the appropriate values.

print(template.format(name=name, planet=planet, gravity=gravity))



# ----------------------------------------------------------------------


# Arithmetic operators in Python
# Python provides common arithmetic operators so you can perform mathematic operations in your code. These include the four core operations of addition, subtraction, multiplication, and division.

# Let's explore how we can create a program that can calculate the distance between two planets. We'll start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Note: Remove the commas when you're using the values.

# Create variables to store the distances
# Start by creating two variables named first_planet and second_planet. Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.

first_planet = 149597870
second_planet = 778547200

# Display distance between planets
# You have two variables which store the distance between each planet and a common point: the sun. You can subtract these two values to determine the distance between the planets.

# Start by adding the code to subtract first_planet from second_planet and store the result in a variable named distance_km. Display the value to the screen.

# Then add the code to convert distance_km to miles by dividing it by 1.609344 (the rough difference between miles and kilometers) and store the result in a variable named distance_mi. Display the value to the screen.

distance_km = second_planet - first_planet
print(distance_km)
distance_mi = distance_km / 1.609344
print(distance_mi)



# ----------------------------------------------------------------------


# Create an application to work with numbers and user input
# You'll frequently need to convert string values into numbers to properly perform different operations, or determine the absolute value of a number. In this exercise, you will create a project to calculate the distance between two planets based on user input.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Read the values from the user
# To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.

# Start by adding the code to prompt the user for the distance between the sun and the first planet, and then the second. Store each result in variables named first_planet_input and second_planet_input.

first_planet_input = input('Enter de distance from the sun for the first planet in KM')
second_planet_input = input('Enter de distance from the sun for the second planet in KM')

# Convert to number
# Because input returns string values, we need to convert them to numbers. Add the code to convert each input into an integer using int. Store the values in first_planet and second_planet respectively.

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)


# Perform the calculation and convert to absolute value
# With your values stored as numbers, you can now add the code to perform the calculation, subtracting the first planet from the second. Because the second planet might be a greater number, you'll use abs to convert it to an absolute value.

# Subtract first_planet from second_planet and convert the result to its absolute value by using abs. Store the result in a variable named distance_km. Then display the result on the screen.

distance_km = first_planet - second_planet
print(abs(distance_km))




# ----------------------------------------------------------------------


# Exercise: Use lists to store planet names
# Lists allow you to store multiple values in a single variable. In this notebook you'll create a project to display information about the planets.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Add all planets to a list
# First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:

# Mercury
# Venus
# Earth
# Mars
# Jupiter
# Saturn
# Uranus
# Neptune
# Finish by using print to display the list of planets.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)

# Display the number of planets
# Next, display the total number of planets by using len and print.

planets_len = len(planets)
print(planets_len)

# or
print("There are", len(planets), "planets")

# Add a planet to the list
# Finally, add Pluto to the list that you created. Then display both the number of planets and the last planet in the list.

planets.append("Pluto")
print("Actually, there are", len(planets), "planets")
print(planets[-1], "is the last planet")




# ----------------------------------------------------------------------


# Use slices to retrieve portions of a list
# You might need to work different sections of a list. In this notebook, you will create a project to display planets closer to and farther away from the sun than a planet that the user enters.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Create the list of planets
# First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:

# Mercury
# Venus
# Earth
# Mars
# Jupiter
# Saturn
# Uranus
# Neptune

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Prompt the user for the reference planet
# Next you will add the code to prompt the user for the name of a planet. You will do this by using input. Because strings are case sensitive in Python, ask the user to use a capital letter to start the name of the planet.

planets_input = input("Insert planet name using capital letter to start the name of the planet")

# Find the location of the selected planet
# Now it's time to determine which planets are closer than the one that the user entered. To do this, you need to find where he planet is in the list. You can use the index method to perform this operation. Add the code to find the index of the planet, and store it in a variable named planet_index.

planet_index = planets.index(planets_input)

# Display planets closer to the sun
# With the index determined, you can now add the code to display planets closer to the sun than the one selected. Use the slicing abilities of a list to display all planets up to the one selected.

print("Here are the planets closer than " + planets_input)
print(planets[0:planet_index])

# Display planets further
# You can use the same index to display planets farther from the sun. However, remember that the starting index is included when you're using a slice. As a result, you'll have to add 1 to the value. Add the code to display the planets farther from the sun.

print("Here are the planets farther than " + planets_input)
print(planets[planet_index + 1:])




# ----------------------------------------------------------------------


# Exercise: Create and modify a Python dictionary
# Python dictionaries allow you to model more complex data. Dictionaries are a collection of key/value pairs, and are very common in Python programs. Their flexibility allows you to dynamically work with related values without having to create classes or objects.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Managing planet data
# You want to create a program which will store and display information about planets. To start you will use one planet. Create a variable named planet. Store the following values as a dictionary:

planet = {
    'name': 'Mars',
    'moons': 2
}

# Display planet data
# With the variable created, you will now display information. You can retrieve information by either using get or square brackets ([ ]) and the key name. Add the code to display the planet information in the following format:

# has moon(s)

# If you were working with Earth, the output would be Earth has 1 moon(s)

print(f'{planet["name"]} has {planet["moons"]} moons(s)')

# Add circumference information
# You can update existing keys or create new ones by either using the update method or using square brackets ([ ]). When you're using update, you pass in a new dictionary object with the updated or new values. When using square brackets, you specify the key name and assign a new value.

# Add a new value to planet with a key of 'circumference (km)'. This new value should store a dictionary with the planet's two circumferences:

# polar: 6752
# equatorial: 6792
# Finally, add the code to print the polar circumference of the planet. You can use whatever sentence formatting you wish.

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(planet['circumference (km)']['polar'])





# ----------------------------------------------------------------------



# Calculating values
# In this scenario, you will calculate both the total number of moons in the solar system and the average number of moons a planet has. You will do this by using a dictionary object.

# This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

# Start by creating a variable named planet_moons as a dictionary with the following key/values:

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Obtain a list of moons and number of planets
# Python dictionaries allow you to retrieve all the values and keys by using the values and keys methods, respectively. Each method returns a list containing the data, which can then be used like a regular Python list. You can determine the number of items by using len, and iterate through it by using for loops. In the dictionary you created, the planet names are keys and the number of moons are the values.

# Start by retrieving a list with the number of moons, and store this in a variable named moons. Then obtain the total number of planets and store that value in a variable named total_planets.

moons = planet_moons.values()
total_planets = len(planet_moons.keys())


# Determine the average number of moons
# You will finish this exercise by determining the average number of moons. Start by creating a variable named total_moons; this will be your counter for the total number of moons. Then add a for loop to loop through the list of moons, adding each value to total_moons. Finally, calculate the average by dividing total_moons by total_planets and displaying the value.

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')



# ----------------------------------------------------------------------


# Exercise: Work with arguments in functions
# Required arguments in functions are used when functions need those arguments to work properly. In this exercise, you'll construct a fuel report that requires information from several fuel locations throughout the rocket ship.
# Create a report generation function
# Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.

# Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:

# Fuel report:
#     Main tank: ##
#     External tank: ##
#     Hydrogen tank: ##

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)


# Run the function
# With the function created, add the code to run the function with the following values:

# Main tank: 80
# External tank: 70
# Hydrogen tank: 75

generate_report(80, 70, 75)



# ----------------------------------------------------------------------


# Exercise: Work with keyword arguments in functions
# In the prior exercise you created a report for a ship with three fuel tanks. What happens if the ship has multiple tanks? Keyword arguments can be a perfect solution for this type of a situation. With keyword arguments a caller can provide multiple values which your code can interact with.

## Create an updated fuel report function

# Create a new function named `fuel_report`. The function will accept a keyword arguments parameter named `fuel_tanks`. Add the code to loop through the entries provided to generate the following output, where `name` is the name of the keyword argument and `value` is the value:

# name: value
# name: value

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

# Call the function
# With the function created, it's time to call it! Pass in the following values for the keyword arguments:

# main = 50
# external = 100
# emergency = 60

(fuel_report(main=50, external=100, emergency=60))