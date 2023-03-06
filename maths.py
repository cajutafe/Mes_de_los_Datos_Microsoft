# Suma
# Python usa para + indicar la suma. Usar + entre dos números los suma y proporciona el total.

answer = 15 + 15
print(answer)
# Output: 30

# Resta
# De manera similar, Python utiliza - para la resta. Usar - entre dos números los resta y proporciona la diferencia.

difference = 30 - 12
print(difference)
# Output: 18

# Multiplicación
# En Python, * es el operador de multiplicación. Proporciona el producto de dos números:

product = 30 * 12
print(product)
# Output: 360

# División
# Por último, / se usa para la división. Proporciona el cociente de dos números:

quotient = 30 / 12
print(quotient)
# Output: 2.5

# Uso de la división
# Imagine que debe convertir un número de segundos en minutos y segundos para su visualización.

seconds = 1042
display_minutes = seconds // 60 # Se usa el doble "//" para redondear el número
print(display_minutes)
# Output: 17

# El paso siguiente es determinar el número de segundos. Este número es el resto de 1042 si divide entre 60. Para encontrar el resto, use el operador módulo, que en Python es %. El resto de 1042 / 60 es 22, que es el valor que el operador módulo proporcionará.

display_seconds = seconds % 60
print(display_seconds)
# Output: 22

# Durante las operaciones se recomienda el uso de paréntesis ya que es una manera más aclarativa y ordenada para entender las operaciones y así saber cual se realizará primero.
 
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
print(result_1, result_2)
# The answer is the same in both cases - 1084



# Conversión de cadenas en números
# Python admite dos tipos principales de números: números enteros (o int) y número de punto flotante (o float). La diferencia clave entre ambos es la existencia de un separador decimal; los enteros son números enteros, mientras que los números de punto flotante contienen un valor decimal.

# Al convertir cadenas en números, debe indicar el tipo de número que desea crear. Tiene que decidir si necesita un separador decimal. Se usa int para realizar la conversión en un número entero y float para hacerlo en un número de punto flotante.

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)
# Output:
# 215
# 215.3

# Valores absolutos
# Use abs para convertir el valor negativo en su valor absoluto. Si hace la misma operación mediante abs (e imprime las respuestas), verá que muestra 23 para ambas ecuaciones.

ex1 = 39 - 16
ex2 = 16 - 39
print(abs(ex1))
print(abs(ex2))
# Output ambos = 23


# Redondeo
# También es útil la función integrada de Python denominada round. Úsela para redondear hacia arriba al entero más cercano si el valor decimal es .5 o mayor, o bien hacia abajo si es menor que .5.

print(round(14.5))
# Output: 15



# Biblioteca matemática
# Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados. Una de las más comunes es la biblioteca math. math permite hacer el redondeo con floor y ceil, proporcionar el valor de pi y muchas otras operaciones. Veamos cómo usar esta biblioteca para redondear hacia arriba o hacia abajo.

# El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor.

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
#Output: 13 y 12