# Funciones sin argumentos
# Para crear una función, use la palabra clave def, seguida de un nombre, paréntesis y, después, del cuerpo con el código de función:

def rocket_parts():
    print("payload, propellant, structure")

# En este caso, rocket_parts es el nombre de la función. Ese nombre va seguido de paréntesis vacíos, que indican que no se necesitan argumentos. El último es el código, con sangría de cuatro espacios. Para usar la función, debe llamarla por su nombre usando paréntesis:

print(rocket_parts())

# La función rocket_parts() no toma ningún argumento e imprime una instrucción sobre la gravedad. Si necesita usar un valor que devuelve una función, puede asignar la salida de la función a una variable:
# >>> output = rocket_parts()
# payload, propellant, structure
# >>> output is None
# True

# Puede parecer sorprendente que el valor de la variable output sea None. Esto se debe a que la función rocket_parts() no ha devuelto explícitamente un valor. En Python, si una función no devuelve explícitamente un valor, devuelve implícitamenteNone. Actualizar la función para devolver la cadena en lugar de imprimirla hace que la variable output tenga un valor distinto:

def rocket_parts2():
    return "playload, propellant, structure"

print(rocket_parts2())
# >>> output = rocket_parts()
# payload, propellant, structure


# Uso de argumentos de función en Python
# Exigencia de un argumento
# Si va a pilotar un cohete, una función sin entradas obligatorias es como un equipo con un botón que le indique la hora. Si presiona el botón, una voz computarizada le indicará la hora. Pero una entrada necesaria puede ser un destino para calcular la distancia del viaje. Las entradas obligatorias se denominan argumentos para la función.

# Para requerir un argumento, póngalo entre paréntesis:

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
# Intente llamar a la función distance_from_earth() sin ningún argumento:

# print(distance_from_earth())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: distance_from_earth() missing 1 required positional argument: 'destination'

print(distance_from_earth("Moon")) # 238,855
print(distance_from_earth("Mars")) # Unable to compute to that destination

# Varios argumentos necesarios
# Para usar varios argumentos, debe separarlos con una coma. Vamos a crear una función que pueda calcular cuántos días se tardarán en llegar a un destino, dadas la distancia y una velocidad constante:

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

# Ahora use la distancia entre la Tierra y la Luna para calcular cuántos días tardaría en llegar a la Luna con un límite de velocidad común de 120 kilómetros por hora:
print(days_to_complete(238855, 75)) # 132.69722222222222

# Funciones como argumentos
# Puede usar el valor de la función days_to_complete() y asignarlo a una variable y, después, pasarlo a round() (una función integrada que redondea al número entero más cercano) para obtener un número entero:

total_days = days_to_complete(238855, 75)
print(round(total_days))

# Pero un patrón útil es pasar funciones a otras funciones en lugar de asignar el valor devuelto:

print(round(days_to_complete(238855, 75)))