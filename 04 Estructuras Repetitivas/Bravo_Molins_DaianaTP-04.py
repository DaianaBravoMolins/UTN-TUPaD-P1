# Bravo Molins Daiana Mariel - Práctico 4: Estructuras repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (0, 100):
#     print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# contadorDigitos = 0
# numeroIngresado = int(input("Ingrese por favor, un numero entero: "))

# if numeroIngresado == 0:
#     contadorDigitos = 0
# elif numeroIngresado < 0:
#     numeroIngresado = abs(numeroIngresado) #funcion "abs" para retornar el valor absoluto del num, sino no funciona con negativos

# while numeroIngresado != 0: 
#     numeroIngresado = numeroIngresado // 10
#     contadorDigitos += 1

# print("El numero tiene ", contadorDigitos, " digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# primerIngreso = int(input("Ingrese un primer numero: "))
# segundoIngreso = int(input("Ingrese un segundo numero: "))
# acumulador = 0

# for i in range(primerIngreso+1, segundoIngreso):
#     acumulador += i

# print("La suma de numero es de: ",acumulador)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# numeroIngresado = int(input("Por favor ingrese un numero (0 para finalizar): "))
# sumasSucesivas = 0 #Acumulador
# bandera = True

# if numeroIngresado == 0:
#     print("No se pueden hacer sumas (numero fuera de rango solicitado).")
# else:
#     while numeroIngresado != 0:
#         sumasSucesivas += numeroIngresado
#         numeroIngresado = int(input("Ingrese otro numero distinto de cero (o cero para finalizar): "))
#         if numeroIngresado == 0:
#             bandera = False
#             break  

# if bandera == False:
#     print("El resutlado de las sumas sucesivas es de: ", sumasSucesivas)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random

# numeroAleatorio = random.randint(0,9)
# contador = 0
# numeroElegido = -1
# bandera = True

# while numeroAleatorio != numeroElegido:
#     numeroElegido = int(input("Ingrese un numero entre 0 y 9 (inclusive): "))
#     if not(0 <= numeroElegido <= 9):
#         print("Numero fuera de rango.")
#         break
#     else: 
#         contador += 1
#         bandera = False        #Recien cunado se adivine el num aleatorio, la bandera se va a usar para el print
#         print("Vamos ! Reintente.")

# if bandera == False:
#     print("Acerto, el numero elegido es",numeroAleatorio,"y la cantidad de intentos hasta adivinar fue de",contador)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, 0, -1):
#     if i % 2 == 0:
#         print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# numeroIngresado = int(input("Ingrese un numero entero positivo: "))
# acumulador = 0

# if numeroIngresado <= 0:
#     print("Numero fuera de rango.")

# for i in range (0,numeroIngresado+1):
#     acumulador += i     #aca se van sumando en forma sucesiva los ingresos
#     bandera = False


# print("La suma sucesiva de numeros desde 0 hasta el n° elegido es de",acumulador)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# contadorPositivos = 0
# contadorNegativos = 0
# contadorPares = 0
# contadorImpares = 0
# bandera = True

# for numero in range(10):
#     numero_ingresado = int(input("Ingrese un numero (menos el cero): "))
#     if  numero_ingresado == 0:
#         print("El numero elegido no es el correcto.")
#         bandera = False
#         break
#     elif numero_ingresado > 0:
#         contadorPositivos += 1
#     else:
#         contadorNegativos += 1

#     if numero_ingresado % 2 == 0:
#         contadorPares += 1
#     elif numero_ingresado % 2 != 0:
#         contadorImpares += 1

# if bandera == True:
#     print("De acuerdo con los numero ingresados: hay", contadorPositivos, "numeros positivos",contadorNegativos, "numeros negativos", contadorPares, "numeros pares y",contadorImpares, "numeros impares.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# acumulador = 0

# for numero in range (100):
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

# media = acumulador/100
# print("La media del conjunto de numeros ingresados es de",media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# numeroIngresado = int(input("Ingrese un numero: "))
# numeroInvertido = 0

# while numeroIngresado > 0:
#     cifra = numeroIngresado % 10       #El resto es el ultimo numero 123%10 = 3
#     numeroInvertido = numeroInvertido*10 + cifra #calculo para ir acomodando las cifras= 3
#     numeroIngresado = numeroIngresado // 10 #Division entera para dejar de lado la ultima cifra 123//10 = 12

# print("El numero invertido es: ",numeroInvertido)










