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



# Uso de argumentos de palabra clave en Python
# Los argumentos opcionales requieren un valor predeterminado asignado a ellos. Estos argumentos con nombre se denominan argumentos de palabra clave. Los valores del argumento de palabra clave deben definirse en las propias funciones. Cuando se llama a una función definida con argumentos de palabra clave, no es necesario usarlos en absoluto.

# La misión Apolo 11 tardó unas 51 horas en llegar a la Luna. Vamos a crear una función que devuelva la hora estimada de llegada usando el mismo valor que la misión Apolo 11 como valor predeterminado:

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

# La función usa el módulo datetime para definir la hora actual. Usa timedelta para permitir la operación de suma que da como resultado un objeto de hora nuevo. Después de calcular ese resultado, devuelve la estimación arrival con formato de cadena. Intente llamarla sin ningún argumento:

print(arrival_time()) # Arrival: Wednesday 13:30

# Aunque la función define un argumento de palabra clave, no permite pasar uno cuando se llama a una función. En este caso, la variable hours tiene como valor predeterminado 51. Para comprobar que la fecha actual es correcta, use 0 como valor para hours:

print(arrival_time(hours=0)) #Devuelve la hora actual Arrival: Monday 10:31

# Combinación de argumentos y argumentos de palabra clave
# A veces, una función necesita una combinación de argumentos de palabra clave y argumentos. En Python, esta combinación sigue un orden específico. Los argumentos siempre se declaran primero, seguidos de argumentos de palabra clave.

# Actualice la función arrival_time() para que tome un argumento necesario, que es el nombre del destino:

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

# Dado que ha agregado un argumento necesario, ya no es posible llamar a la función sin ningún argumento:

# print(arrival_time())
# TypeError: arrival_time() missing 1 required positional argument: 'destination'

# Use "Moon" como valor para destination a fin de evitar el error:

print(arrival_time("Moon")) # Moon Arrival: Wednesday 13:39

# También puede pasar más de dos valores, pero debe separarlos con una coma. Se tarda aproximadamente 8 minutos (0,13 horas) en entrar en órbita, así que utilice eso como argumento:

print(arrival_time("Orbit", hours=0.13)) # Orbit Arrival: Monday 10:49




# Uso de argumentos de variable en Python
# En Python, puede usar cualquier número de argumentos de palabra clave y argumentos sin necesidad de declarar cada uno de ellos. Esta capacidad es útil cuando una función puede obtener un número desconocido de entradas.

# Argumentos de variable
# Los argumentos en las funciones son necesarios. Pero cuando se usan argumentos de variable, la función permite pasar cualquier número de argumentos (incluido 0). La sintaxis para usar argumentos de variable es agregar un asterisco único como prefijo (*) antes del nombre del argumento.

# La función siguiente imprime los argumentos recibidos:

def variable_length(*args):
    print(args)

# En este caso, *args indica a la función que acepte cualquier número de argumentos (incluido 0). En la función, args ahora está disponible como la variable que contiene todos los argumentos como una tupla. Pruebe la función pasando cualquier número o tipo de argumentos:

print(variable_length()) # ()
print(variable_length("one", "two")) # ('one', 'two')
print(variable_length(None)) # (None, )

# Como puede ver, no hay ninguna restricción en el número o tipo de argumentos que se pasan.

# Un cohete realiza varios pasos antes de un lanzamiento. En función de las tareas o retrasos, estos pasos pueden tardar más de lo previsto. Vamos a crear una función de longitud variable que pueda calcular cuántos minutos quedan hasta el inicio, dado el tiempo que va a tardar cada paso:

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
# Pruebe la función pasando cualquier número de minutos:

print(sequence_time(4, 14, 18)) # Total time to launch is 36 minutes
print(sequence_time(4, 14, 48)) # Total time to launch is 1.1 hours

# Argumentos de palabra clave variable
# Para que una función acepte cualquier número de argumentos de palabra clave, debe usar una sintaxis similar. En este caso, se requiere un asterisco doble:

def variable_length(**kwargs):
    print(kwargs)

# Pruebe la función de ejemplo, que imprime los nombres y valores pasados como kwargs:

print(variable_length(tanks=1, day="Wednesday", pilots=3)) # {'tanks': 1, 'day': 'Wednesday', 'pilots': 3}


# En esta función, vamos a usar argumentos de palabra clave variable para notificar los astronautas asignados a la misión. Dado que esta función permite cualquier número de argumentos de palabra clave, se puede reutilizar independientemente del número de astronautas asignados:

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

# Pruébalo con la tripulación del Apolo 11:

print(crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"))
# 3 astronauts assigned for this mission:
# captain: Neil Armstrong
# pilot: Buzz Aldrin
# command_pilot: Michael Collins