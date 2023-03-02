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