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

# ----------------------------------------------------------------------

# BOOLEANOS

# Expresiones "if"

a = 97
b = 55
# Test expression
if a < b: # Si "a" es menor que "b" pintame "b"
    # Statement to be run
    print(b) # No lo pinta porque el resultado booleanos no es "True"

# En el siguiente caso la expresión "if" sin cumple por lo que se acaba ejecutando
c = 93
d = 27
if c >= d:
    print(c)

# Siempre importante las sangrias: En este ejemplo, la salida es 44 ya que la expresión de prueba es False y la instrucción print(b) no tiene sangría en el mismo nivel que la instrucción if.

e = 24
f = 44
if e <= 0:
    print(e)
print(f)

#Añadimos "else" para que nos imprima las acciones "false"

g = 93
h = 27
if g >= h:
    print(g)
else:
    print(h)
