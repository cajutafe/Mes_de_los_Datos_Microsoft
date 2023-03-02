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

# Formato de signo de porcentaje (%)
# El marcador de posición de la variable de la cadena es %s. Después de la cadena, use otro carácter % seguido del nombre de la variable. En el ejemplo siguiente, se muestra cómo dar formato mediante el carácter %:

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
# On the Moon, you would weigh about 1/6 of your weight on Earth

# El uso de varios valores cambia la sintaxis, ya que se necesitan paréntesis para rodear las variables que se pasan:

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

# El método format()
# El método .format() usa llaves ({}) como marcadores de posición dentro de una cadena y utiliza la asignación de variables para reemplazar texto.

mass_percentage2 = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage2))
#On the Moon, you would weigh about 1/6 of your weight on Earth

# No es necesario asignar variables repetidas varias veces, lo que hace que sea menos detallado porque es necesario asignar menos variables:

print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
# You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

# En lugar de llaves vacías, la sustitución consiste en usar números. {0} significa usar el primer argumento (índice cero) de .format(), que en este caso es Moon. {0} funciona bien para una repetición simple, pero reduce la legibilidad. Para mejorar la legibilidad, use argumentos de palabra clave en .format() y, después, haga referencia a los mismos argumentos entre llaves:

print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
#You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

# Acerca de las cadenas f-strings
# A partir de la versión 3.6 de Python, es posible usar f-strings. Estas cadenas parecen plantillas y usan los nombres de variable del código. El uso de f-strings en el ejemplo anterior tendría el siguiente aspecto:

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
#On the Moon, you would weigh about 1/6 of your weight on Earth

# Con f-strings, no es necesario asignar un valor a una variable de antemano:

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
#On the Moon, you would weigh about 16.7% of your weight on Earth

# Para usar una expresión no es necesaria una llamada de función. Cualquiera de los métodos de cadena también son válidos. Por ejemplo, la cadena podría aplicar un uso específico de mayúsculas y minúsculas para crear un título:

subject = "interesting facts about the moon"
print(f"{subject.title()}")
# 'Interesting Facts About The Moon'