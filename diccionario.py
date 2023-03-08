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