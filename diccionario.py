# Creación de diferentes variables en las cuales tardaríamos mucho en encontrar y reproducir la clave-valor de las diferentes variables, es por esto que se usan los diccionarios en Python

name = 'Earth'
moons = 1

earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

# CREACIÓN DE UN DICCIONARIO

planet = {
    'name': 'Earth',
    'moons': 1
} #Tiene dos claves, 'name' y 'moons'. Cada clave se comporta igual que una variable: tienen un nombre único y almacenan un valor. Pero se incluyen dentro de una única variable más grande, denominada planet.

print(planet.get('name'))
#Otro método más común entre programadores
print(planet['name']) #EARTH

# wibble = planet.get('wibble') #Returs None
# wibble = planet['wibble'] #Da KeyError

# Modificación de valores de diccionario
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

planet['name'] = 'Jupiter'
planet['moons'] = 79

print(planet['name']) #JUPITER


# ADICIÓN Y ELIMINACIÓN DE CLAVES.
# Queremos actualizr 'planet' para incluir el período orbital en días:
planet['orbital period'] = 4333
print(planet['orbital period'])

# Para eliminar usas 'pop'

planet.pop('orbital period')
# print(planet['orbital period']) # KeyError por haberlo borrado


# Tipos de data complejos
#Añadimos un diccionario dentro de planet
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# Recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


# Programación dinámica con diccionarios
# Recuperación de todas las claves y valores

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# Imagine que quiere mostrar la lista de todas las precipitaciones. Puede escribir el nombre de cada mes, pero resultará tedioso.

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Determinación de la existencia de una clave en un diccionario
# Al actualizar un valor en un diccionario, Python sobrescribirá el valor existente o creará uno, si la clave no existe. Si quiere agregar a un valor en lugar de sobrescribirlo, puede comprobar si la clave existe mediante in. Por ejemplo, si quiere agregar un valor a diciembre o crear uno si no existe, puede usar lo siguiente:

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
print(rainfall['december'])

# Recuperación de todos los valores
# De forma similar a keys(), values() devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes. values() puede resultar útil cuando se usa la clave con fines de etiquetado, como en el ejemplo anterior, en el que las claves son el nombre del mes. Puede usar para values() determinar el importe total de las precipitaciones:

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter')