#Bravo Molins Daiana Mariel
#TP 3 Condicionales

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# # edadUsuario = int(input("Por favor ingrese su edad: "))

# if edadUsuario >= 18:
#     print("Es mayor de edad.")
# else:
#     pass


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# notaUsuario = int(input("Ingrese su nota, por favor: "))

# if notaUsuario >= 6:
#     print("Aprobado.")
# else:
#     print("Desaprobado.")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numeroIngresado = int(input("Ingrese un numero par, por favor: "))

# if numeroIngresado % 2 == 0:
#     print("Ha ingresado un numero par.")
# else:
#     print("Por favor, ingrese un número par.")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edadUsuario = int(input("Ingrese su edad: "))

# if edadUsuario < 12:
#     print("Niño/a")
# elif edadUsuario >= 12 and edadUsuario < 18:
#     print("Adolescente")
# elif edadUsuario >= 18 and edadUsuario < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contraseñaIngresada = input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: ")

# if len(contraseñaIngresada) >= 8 and len(contraseñaIngresada) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# from statistics import median, mode, mean
# import random

# numeros_aleatorios = [random.randint(1,100) for i in range(50)]

# mediana = median(numeros_aleatorios)
# print("Mediana:",mediana)
# moda = mode(numeros_aleatorios)
# print("Moda:",moda)
# media = mean(numeros_aleatorios)
# print("Media:",media)

# if media > mediana and mediana > moda:
#     print("sesgo positivo.")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo")
# elif media == moda and moda == mediana:
#     print("No hay sesgo.")
# else:
#     pass

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# fraseIngresada = input("Por favor ingrese una frase o palabra: ")

# vocal = ["a", "e", "i", "o", "u"]

# if fraseIngresada[-1] in vocal:
#     print(fraseIngresada, "!")
# else:
#     print(fraseIngresada)

#variante:

# fraseIngresada = input("Por favor ingrese una frase o palabra: ")

# vocalA ="a"
# vocalE ="e"
# vocalI ="i"
# vocalO ="o"
# vocalU ="u"

# if fraseIngresada[-1] == vocalA or fraseIngresada[-1] == vocalE or fraseIngresada[-1] == vocalI or fraseIngresada[-1] == vocalO or fraseIngresada[-1] == vocalU:
#     print(fraseIngresada, "!")
# else:
#     print(fraseIngresada)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas

# nombreIngresado = input("Ingrese por favor, su nombre: ")
# opcionElegida = int(input("Ingrese 1 para su nombre en mayuscula, 2 para minuscula o 3 para solo la primer letra en mayuscula: "))

# if opcionElegida == 1:
#     print(nombreIngresado.upper())
# elif opcionElegida == 2:
#     print(nombreIngresado.lower())
# elif opcionElegida == 3:
#     print(nombreIngresado.title())
# else:
#     pass


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitudTerremoto = int(input("Ingrese la magnitud del terremoto: "))

# if magnitudTerremoto < 3:
#     print("Muy leve.")
# elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
#     print("Leve.")
# elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
#     print("Moderado.")
# elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
#     print("Fuerte.")
# elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
#     print("Muy fuerte.")
# else:
#     print("Extremo.")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año Estación en el
# hemisferio norte
# Estación en el
# hemisferio sur
# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos) Invierno Verano
# Desde el 21 de marzo hasta el 20 de junio
# (incluidos) Primavera Otoño
# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos) Verano Invierno
# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos) Otoño Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano

# abril, junio, septiembre y noviembre: 30 días
# enero, marzo, mayo, julio, agosto, octubre, diciembre: 31 días
# febrero: 28 días.

#variante
hemisferioElegido = input("Ingrese en que hemisferio se encuentra: N para norte o S para sur: ")
mesElegido = input("Ingrese el mes actual: ")
diaElegido = int(input("Ingrese el dia actual: "))

opcion1 = (mesElegido.lower() == "diciembre" and 21 <= diaElegido <= 31) or (mesElegido.lower() == "enero" and 1 <= diaElegido <= 31) or (mesElegido.lower() == "febrero" and 1 <= diaElegido <= 28) or (mesElegido.lower() == "marzo" and 1 <= diaElegido <= 20)

opcion2 = (mesElegido.lower() == "marzo" and 21 <= diaElegido <= 31) or (mesElegido.lower() == "abril" and 1 <= diaElegido <= 30) or (mesElegido.lower() == "mayo" and 1<= diaElegido <= 31) or (mesElegido.lower() == "junio" and 1 <= diaElegido <= 20)

opcion3 =  (mesElegido.lower() == "junio" and 21 <= diaElegido <=30) or (mesElegido.lower() == "julio" and 1 <= diaElegido <= 31) or (mesElegido.lower() == "agosto" and 1<= diaElegido <= 31) or (mesElegido.lower() == "septiembre" and 1 <= diaElegido <= 20)

opcion4 = (mesElegido.lower() == "septiembre" and 21 <= diaElegido <=30) or(mesElegido.lower() == "octubre" and 1 <= diaElegido <= 31) or (mesElegido.lower() == "noviembre" and 1<= diaElegido <= 30) or (mesElegido.lower() == "diciembre" and 1<= diaElegido <= 20)

if hemisferioElegido.upper() == "N":
    if opcion1 == True:
        print("Invierno")
    elif opcion2 == True:
        print("Primavera")
    elif opcion3 == True:
        print("Verano")
    elif opcion4 == True:
        print("Otoño")
    else:
        print("Algun dato es erroneo")
elif hemisferioElegido.upper() == "S":
    if opcion1 == True:
        print("Verano")
    elif opcion2 == True:
        print("Otoño")
    elif opcion3 == True:
        print("Invierno")
    elif opcion4:
        print("Primavera")
    else:
        print("Algun dato es erroneo")
else:
    print("La letra ingresada para el hemisferio es erronea.")
