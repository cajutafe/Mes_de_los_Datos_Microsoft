# Los métodos de cadena forman parte del tipo str. Esto significa que los métodos existen como variables de cadena o directamente como parte de la cadena. Por ejemplo, el método .title() se puede usar directamente con una cadena:

heading = "temperatures and facts about the moon"
print(heading)
print(heading.title())


# Un método de cadena común es .split(). Sin argumentos, el método separará la cadena en cada espacio. Esto crearía una lista de todas las palabras o números separados por un espacio:

temperatures = """Daylight: 260 F 
Nighttime: -280 F"""
print(temperatures .split())
print(temperatures .split('\n')) #Este tipo de división resulta útil cuando se necesita un bucle para procesar o extraer información, o bien cuando se cargan datos desde un archivo de texto.


# Búsqueda de una cadena
# La manera más sencilla de detectar si existe una palabra, un carácter o un grupo de caracteres determinados en una cadena es usar el operador in:

# >>> "Moon" in "This text will describe facts and challenges with space travel"
# False
# >>> "Moon" in "This text will describe facts about the Moon"
# True

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
# El método .find() devuelve -1 cuando no se encuentra la palabra, o bien devuelve el índice (el número que representa la posición en la cadena). Así es como se comportaría si busca la palabra Mars:
print(temperatures.find("Mars"))

# Otra manera de buscar contenido consiste en usar el método .count(), que devuelve el número total de repeticiones de una palabra determinada en una cadena:
print(temperatures.count("Moon"))
print(temperatures.count("Mars"))

# Las cadenas en Python distinguen mayúsculas de minúsculas, lo que significa que Luna y luna se consideran palabras diferentes. Para realizar una comparación sin distinguir mayúsculas de minúsculas, puede convertir una cadena en letras minúsculas mediante el método .lower():

ejemplo_lower = "The Moon And The Earth".lower()
print(ejemplo_lower)

# Como sucede con el método .lower(), las cadenas tienen un método .upper() que hace lo contrario y convierte todos los caracteres en mayúsculas:

ejemplo_upper = "The Moon And The Earth".upper()
print(ejemplo_upper)


# Comprobación del contenido
# Hay ocasiones en las que procesará texto para extraer información con una presentación irregular. Por ejemplo, la cadena siguiente es más fácil de procesar que un párrafo no estructurado:

temperatures2 = "Mars Average Temperature: -60 C"
# Para extraer la temperatura media en Marte, puede hacerlo con los métodos siguientes:

parts = temperatures2.split(':')
print(parts) # ['Mars average temperature', ' -60 C']
print(parts[-1]) # ' -60 C'

# El código anterior confía en que todo lo que hay después de los dos puntos (:) es una temperatura. La cadena se divide en :, lo que genera una lista de dos elementos. El uso de [-1] en la lista devuelve el último elemento que, en este ejemplo, es la temperatura.

# Si el texto es irregular, no puede usar los mismos métodos de división para obtener el valor. Debe recorrer en bucle los elementos y comprobar si los valores son de un tipo determinado. Python tiene métodos que ayudan a comprobar el tipo de cadena:

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item) #30

# Como sucede con el método .isnumeric(), .isdecimal() puede buscar cadenas que parezcan decimales.


# El método .join() necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print('\n'.join(moon_facts))
# 'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'