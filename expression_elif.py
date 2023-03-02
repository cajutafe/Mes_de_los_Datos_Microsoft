# Uso de elif
# En Python, la palabra clave elif es la abreviatura de else if. El uso de instrucciones elif permite agregar varias expresiones de prueba al programa. Estas instrucciones se ejecutan en el orden en que se escriben, por lo que el programa escribirá una instrucción elif solo si la primera instrucción if es False. Por ejemplo:

a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")


# Combinación de instrucciones if, elif y else
# Puede combinar instrucciones if, elif y else para crear programas con lógica condicional compleja. Recuerde que una instrucción elif solo se ejecuta cuando la condición if es false. Tenga en cuenta también que un bloque if solo puede tener un bloque else, pero puede tener varios bloques elif.

# Ahora se volverá a examinar el ejemplo con una instrucción elif agregada:

a = 27
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")



# Uso de lógica condicional anidada
# Python también admite la lógica condicional anidada, lo que significa que puede anidar instrucciones if, elif y else para crear programas aún más complejos. Para anidar condiciones, aplique sangría a las condiciones internas y todo lo que esté en el mismo nivel de sangría se ejecutará en el mismo bloque de código:

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")