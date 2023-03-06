# Crear una lista
# Para crear una lista, asigne una secuencia de valores a una variable. Cada valor está separado por una coma y están entre corchetes ([]). En el ejemplo siguiente se almacena la lista de todos los planetas de la variable planets:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Acceso a elementos de lista por índice
# Puede acceder a cualquier elemento de una lista colocando el índice entre corchetes [] después del nombre de la variable de lista. Los índices comienzan a partir de 0, por lo que en el código siguiente, planets[0] es el primer elemento de la lista planets:

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2
                                     ])
# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

# También puede modificar valores de una lista mediante un índice. Para ello, asigne un nuevo valor, de la misma manera que asignaría un valor de variable. Por ejemplo, podría cambiar el nombre de Marte en la lista para usar su alias:

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
# Output
# Mars is also known as Red Planet


# Determinación de la longitud de una lista
# Para obtener la longitud de una lista, use la función integrada len(). El código siguiente crea una variable, number_of_planets. El código asigna esa variable con el número de elementos de la lista planets (8).

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# Output:
# There are 8 planets in the solar system



# Incorporación de valores a listas
# Las listas de Python son dinámicas: puede agregar y quitar elementos después de crearlas. Para agregar un elemento a una lista, use el método .append(value).

# Por ejemplo, el código siguiente agrega la cadena "Pluto" al final de la lista planets:

planets.append("Pluto")
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# Output:
# There are 9 planets in the solar system

# Eliminación de valores de listas
# Puede quitar el último elemento de una lista llamando al método .pop() en la variable de lista:

planets.pop() #Goodbye, Pluto
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Uso de índices negativos
# Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.

# En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo.

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
# Output
# The last planet is Neptune
# The penultimate planet is Uranus


# Búsqueda de un valor en una lista
# Para determinar dónde se almacena un valor en una lista, use el método index de la lista. Este método busca el valor y devuelve el índice de ese elemento en la lista. Si no encuentra ninguna coincidencia, devuelve -1.

# En el ejemplo siguiente se muestra el uso de "Jupiter" como el valor del índice:

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun") #+1 para que sume el valor al index ya que empieza en 0
# Output: Jupiter is the 5 planet from the sun





# Almacenamiento de números en listas
# Para almacenar números con decimales en Python, se debe usar el tipo float. Para crear un valor float, escriba el número con la posición decimal y asígnelo a una variable:
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
# El código siguiente crea una lista en la que se muestran las fuerzas de los ocho planetas del sistema solar, en G:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# En esta lista, gravity_on_planets[0] es la gravedad en Mercurio (0,378 G), gravity_on_planets[1] es la gravedad en Venus (0,907 G), y así sucesivamente.

# En la Tierra, un autobús de dos pisos pesa 12 650 kilogramos (kg), es decir, 12,65 toneladas. En Mercurio, donde la gravedad es de 0,378 G, el mismo autobús pesa 12,65 toneladas multiplicado por 0,378. En Python, para multiplicar dos valores, se usa el símbolo *.

# En el ejemplo siguiente, puede averiguar el peso de un autobús de dos pisos en diferentes planetas obteniendo el valor de la lista:

bus_weight = 12650 #in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")
# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg


# Uso de min() y max() con listas
# Python tiene funciones integradas para calcular los números más grandes y más pequeños de una lista. La función max() devuelve el número más grande y min() devuelve el más pequeño. Por lo tanto, min(gravity_on_planets) devuelve el número más pequeño de la lista gravity_on_planets, que es 0,377 (Marte).

# El código siguiente calcula los pesos mínimo y máximo en el sistema solar mediante esas funciones:

print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg


# Segmentación de listas
# Puede recuperar una parte de una lista mediante una segmentación. Una segmentación usa corchetes, pero en lugar de un solo elemento, tiene los índices inicial y final. Cuando se usa una segmentación, se crea una lista que comienza en el índice inicial y termina antes del índice final (y no lo incluye).

# La lista de planetas tiene ocho elementos. La Tierra es el tercero de la lista. Para mostrar los planetas que hay antes de la Tierra, use una segmentación a fin de obtener los elementos que empiezan en 0 y terminan en 2:

planets_before_earth = planets[0:2]
print(planets_before_earth)
# Para obtener todos los planetas después de la Tierra, comience en el tercero y vaya hasta el octavo:
planets_after_earth = planets[3:8]
print(planets_after_earth) #En este ejemplo, se muestra Neptuno. La razón es que el índice de Neptuno es 7, porque la indexación comienza en 0. Dado que el índice final era 8, incluye el último valor. Si no coloca el índice de detención en la segmentación, Python asume que quiere ir al final de la lista:
planets_after_earth2 = planets[3:]
print(planets_after_earth2)


# Combinación de listas
# Ha visto cómo puede usar segmentaciones para dividir listas, pero ¿qué sucede con unirlas de nuevo?

# Para unir dos listas, debe usar el otro operador (+) con dos listas para devolver una nueva.

# Hay 79 lunas conocidas de Júpiter. Las cuatro más grandes son Ío, Europa, Ganímedes y Calisto. Estas lunas se denominan lunas galileanas, ya que Galileo Galilei las descubrió con su telescopio en 1610. El grupo de Amaltea está más cerca de Júpiter que el grupo galileano. Consta de las lunas Metis, Adrastea, Amaltea y Tebe.

# Cree dos listas. Rellene la primera lista con las cuatro lunas de Amaltea y la segunda lista con las cuatro lunas galileanas. Únalas mediante + para crear una lista:

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

# Ordenación de listas
# Para ordenar una lista, use el método .sort() de la lista. Python ordenará una lista de cadenas en orden alfabético y una lista de números en orden numérico:

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

# Para ordenar una lista en orden inverso, llame a .sort(reverse=True) en la lista:
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']
print(regular_satellite_moons) #Sort modifica la lista actual.