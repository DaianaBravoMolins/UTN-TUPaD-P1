# # Ejercicio 1: Bucle for para números pares
# # Objetivo: Imprimir números pares usando un bucle for. Instrucciones:
# # 1. Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
# # 2.Usa un condicional o el paso del rango para lograrlo.
# # Preguntas de reflexión:
# # •¿Cómo modificarías el código para imprimir solo impares?
# # •¿Qué pasa si el rango fuera de 2 a 20 con paso 3?

# for i in range(2,21,2):
#     print(i)

# #Pondria como 1er parametro el 1 en lugar de 2. De modo que el ciclo comience con "1".
# #Imprime de a 3 numeros: 2,5,8,11,14,17 (el 20 no esta incluido).

# # Ejercicio 2: Bucle while con suma acumulativa
# # Objetivo: Usar un bucle while para controlar una condición de salida. Instrucciones:
# # 1.Pide al usuario que ingrese números hasta que la suma supere 100.
# # 2.Imprime la suma total al final.
# # Preguntas de reflexión:
# # •¿Qué ocurre si el primer número ingresado es mayor que 100?
# # •¿Cómo evitarías errores si el usuario ingresa texto?

# numero_ingresado =0
# acumulador = 0

# while acumulador < 100:
#     numero_ingresado = int(input("Ingrese numero: "))
#     acumulador += numero_ingresado

# print(acumulador)

# #No entra al ciclo, solo imprime el numero.
# #Yo usaria un try-except o un while que me pida constantemente el reingreso hasta que no sea un string.


# # Ejercicio 3: Filtrar palabras por letra inicial
# # Objetivo: Iterar sobre una lista y aplicar filtros. Instrucciones:
# # 1.Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime solo las que empiezan con "a".
# # Preguntas de reflexión:
# # •¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también se cuente)?
# # •¿Qué método de strings es útil para esto?

# lista = ["apple", "banana", "avocado"]

# for fruta in lista:
#     if fruta[0] == "a":
#         print(fruta)
    
    

# #Agregraria la opcion con mayuscula. EJ: if fruta[0] == "a" or fruta[0] == "A":
# #El metodo .capitalize() permite dejar la primer latra en mayuscula. Ej: if fruta[0].capitalize() == "A"


# # Ejercicio 4: Tabla de multiplicar del 7
# # Objetivo: Usar un bucle para generar patrones. Instrucciones:
# # 1.Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).
# # Preguntas de reflexión:
# # •¿Cómo adaptarías el código para que el usuario elija la tabla?
# # •¿Qué estructura usarías para almacenar los resultados?

# contador = 0

# for numero in range(7,71,7):
#     contador+= 1
#     print(7, "*",contador,"=",numero)

# #Iniciaria una variable en la cual le solicito al usuario que ingrese el numero que quiera para calcular su tabla de multiplicar.
# #Creando una lista vacia antes del ciclo y acumulando los distintos resultados en la misma.

# # Ejercicio 5: Contador de vocales
# # Objetivo: Contar caracteres específicos en un string. Instrucciones:
# # 1.Pide al usuario una cadena de texto.
# # 2.Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.
# # Preguntas de reflexión:¿Cómo manejarías las vocales acentuadas (á, é)?
# # •¿Qué estructura de datos te ayudaría a optimizar el código?

# # palabra_ingresada = input("Ingrese una palabra: ")

# # contador_a = 0
# # contador_e = 0
# # contador_i = 0
# # contador_o = 0
# # contador_u = 0

# # for letra in palabra_ingresada:
# #     if letra == "a":
# #         contador_a += 1
# #     elif letra == "e":
# #         contador_e += 1
# #     elif letra == "i":
# #         contador_i += 1
# #     elif letra == "o":
# #         contador_o += 1
# #     elif letra == "u":
# #         contador_u += 1
    

# # print("La palabra ingresada tiene:",contador_a,"vocal/es a,",contador_e,"vocal/es e,",contador_i,"vocal/es i,",contador_o,"vocal/es o y", contador_u, "vocal/es u.")

# # #Agregaria las opciones con acento.
# # #Se podria usar una lista donde cada elemento fuese una vocal. 

# # # Ejercicio 6: Números repetidos en una lista
# # # Objetivo: Filtrar elementos duplicados manteniendo el orden. Instrucciones:
# # # 1.Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que aparecen más de una vez (en este caso: [3, 1]).
# # # Preguntas de reflexión:
# # # •¿Por qué es importante mantener el orden de aparición?
# # # •¿Cómo resolverías esto sin usar estructuras adicionales?

# # lista =  [3, 1, 3, 5, 1]

# # lista_repetidos = []

# # for numero in lista:
# #     if numero not in lista_repetidos and lista.count(numero) > 1:
# #         lista_repetidos.append(numero)


# # print(lista_repetidos)

# #Para poder ir comparando numeros, a medida que se recorren.
# #Lo dejaria asi:

# # lista =  [3, 1, 3, 5, 1]

# # for numero in lista:
# #     if lista.count(numero) > 1:
# #         lista.remove(numero)

# # print(lista)


# # # Ejercicio 7: FizzBuzz
# # # Objetivo: Implementar lógica condicional en bucles. Instrucciones:
# # # 1.Imprime números del 1 al 100, pero:
# # # o Para múltiplos de 3 → "Fizz".
# # # o Para múltiplos de 5 → "Buzz".
# # # o Para múltiplos de ambos → "FizzBuzz".
# # # Preguntas de reflexión:
# # # •¿Por qué el orden de los condicionales es crucial aquí?
# # # •¿Cómo extenderías el juego a otros números (ej: 7 → "Bazz")?

# # for i in range(1,101,1):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print("FizzBuzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(i)


# # Ejercicio 8: Frecuencia de palabras
# # Objetivo: Usar diccionarios para contar elementos. Instrucciones:
# # 1.
# # Dada una cadena (ej: "hola hola mundo"), devuelve un diccionario con la frecuencia de cada palabra (ej: {"hola": 2, "mundo": 1}).
# # Preguntas de reflexión:
# # •¿Cómo ignorarías signos de puntuación (ej: "hola," vs "hola")?
# # •¿Qué método de strings ayuda a separar palabras?

# cadena = "hola hola mundo"

# palabra = cadena.split()
# print(palabra)

# diccionario = {}

# for palabraindividual in palabra:
#         if palabraindividual not in diccionario:
#             diccionario[palabraindividual] = 1
#         else:
#             diccionario[palabraindividual] = diccionario[palabraindividual]+ 1

# print(diccionario)

# #Diccionario es un tema no visto, la ia me ayudo a explicarme un poco como funciona esta nueva estructura.
# #usaria un palabra[:-1] asi me borra la coma. Se devulve la ultima palabra sin el ultimo caracater.
# #El metodo .split separa la cadena de strings en palabras. 

# # Ejercicio 9: Filtrar consonantes
# # Objetivo: Manipular strings con condiciones. Instrucciones:
# # 1.Dada una cadena, crea una nueva cadena que solo contenga sus consonantes (ej: "Hola" → "Hl").
# # Preguntas de reflexión:
# # • ¿Cómo manejarías las mayúsculas/minúsculas?
# # • ¿Qué estructura usarías para definir las consonantes?


# cadena_1 = ["Hola", "Mundo", "Estudio", "Programacion"]

# nueva_lista = []
# #Recorro cada palabra dentro de la lista
# for palabra in cadena_1: 
#      #variable donde voy a ir guardando las consonantes por palabra 
#     #palabra = palabra.upper()       o palabra = palabra.lower()             
#     print(palabra)
#     palabra_consonantes = ""     
#     #recorro cada letra de cada palabra          
#     for letra in palabra:  
#          #pido las consonantes de cada palabra                    
#         if letra not in "aeiouAEIOU":          
#             #las consonantes encontradas se van a ir juntando por su palabra correspondiente
#             palabra_consonantes = palabra_consonantes + letra   
#             #agrego a la nueva lista solo las palabras como quedaron armadas(solo consonantes)
#     nueva_lista.append(palabra_consonantes)             
            
# print(nueva_lista)

#El codigo esta comentado porque fue dificil armarlo. 
#Maneje el uso de minusculas y mayusculas incluyendo ambos grupos en la comparacion. Otra forma es que la pabrala se le de unformato
#usando .upper (todo mayusculas) o .lower (todo minuscualas), de esta manera solo se trabaja con un grupo de letras con las mismas caracteristicas.


# # Ejercicio 10: Números primos
# # Objetivo: Implementar un algoritmo con bucles anidados. Instrucciones:
# # 1.Pide al usuario un número entero positivo.
# # 2.Imprime todos los números primos menores o iguales a ese número.
# # Preguntas de reflexión:
# # • ¿Cómo optimizarías la verificación de primos?
# # • ¿Qué ventaja tiene usar range(2, int(n**0.5) + 1)?


#FAlta hacer
numero_ingresado = int(input("Ingrese un numero: "))

for numero in range(numero_ingresado):
    if numero_ingresado % numero_ingresado == 0 and numero_ingresado % 1 == 0 and numero_ingresado % 2 != 0:
        print(numero_ingresado)

# Diagrama de flujo: Elige un ejercicio y dibuja su diagrama de flujo.
# •
# Reto extra: Modifica un ejercicio para usar break o continue.