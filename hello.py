print('Hello, World')

# program.py
sum = 1 + 2
print(sum)

print("Show this in the console")

product = sum * 2
print(product) 

# type(sum) Nos muestra el tipo de dato que es


# Operadores mediante los cuales se realizan las operaciones, siempre con la idea de: <left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side #Se usa la barra / para dividir los valores                                                                

# Para trabajar con una fecha, debe importar el módulo date:
from datetime import date
# A continuación, puede llamar a las funciones con las que quiere trabajar. Para obtener la fecha de hoy, puede llamar a la función today():
date.today()
print(date.today())

# Quiere usar una fecha con algo, normalmente una cadena. Si, por ejemplo, desea mostrar la fecha de hoy en la consola, podría experimentar algún problema:
# print("Today's date is: " + date.today())

# Para que este código funcione, debe convertir la fecha en una cadena. Para realizar esta conversión, use la función de utilidad str():
print("Today's date is: " + str(date.today()))


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

# ----------------------------------------------------------------------
# Argumentos de la línea de comandos
# ¿Cómo se capturan estos comandos desde la perspectiva de la codificación? Mediante el módulo sys, puede recuperar los argumentos de la línea de comandos y usarlos en el programa. Observe el código siguiente:

# import sys

# print(sys.argv)
# print(sys.argv[0]) # program name
# print(sys.argv[1]) # first arg

# sys.argv es una matriz o estructura de datos que contiene muchos elementos. La primera posición, que se indica como 0 en la matriz, contiene el nombre del programa. La segunda posición, 1, contiene el primer argumento.



# Entrada de usuario
# Otra manera de pasar datos al programa es hacer que el usuario escriba los datos. Puede codificarlo para que el programa indique al usuario que escriba información. Guarde los datos especificados en el programa y, a continuación, trabaje con ellos.

# Para capturar información del usuario, use la función input(). Este es un ejemplo:

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)



# Trabajo con números
# La función input() almacena un resultado como una cadena, por lo que es posible que el código siguiente no haga lo que quiera:

print("calculator program with chain")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)

# La explicación es que first_number y second_number son cadenas. Para que el cálculo funcione correctamente, debe cambiar esas cadenas a números mediante la función int(). Al modificar la última línea del programa para usar int(), puede resolver el problema:

print(int(first_number) + int(second_number)) #Aquí SÍ suma

