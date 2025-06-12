#Funciones - Bravo Molins Daiana

import funciones

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


#programa principal:
#funciones.imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#programa principal:
# saludo = funciones.saludar_usuario("Daiana")
# print(saludo)


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

#Programa principal:
# nombre_ingresado = input("Ingrese su nombre: ")
# apellido_ingresado = input("Su apellido: ")
# edad_ingresada = input("Su edad: ")
# residencia_ingresada = input("Su residencia: ")

# funciones.informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

#Programa principal:

# radio = int(input("Ingrese el radio de un circulo: "))
# print(funciones.calcular_area_circulo(radio))
# print(funciones.calcular_perimetro_circulo(radio))


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

#Programa principal:

# segundos_ingresados = int(input("Ingrese una cantidad de segundos: "))
# print(funciones.segundos_a_horas(segundos_ingresados))


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# numero_igresado = int(input("Ingrese un numero: "))
# funciones.tabla(numero_igresado)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

#programa principal:

# x = int(input("Por favor, ingrese un primer numero: "))
# y = int(input("Por favor, ingrese un segundo numero."))
# funciones.operaciones_basicas(x,y)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

#programa principal:
# peso_ingresado = float(input("Ingrese su peso: "))
# altura_ingresada = float(input("Ingrese su altura: "))

# funciones.calcular_imc(peso_ingresado, altura_ingresada)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

celsius = float(input("Por favor ingrese la temperatura en grados Celsius: "))

funciones.celsius_a_farenheit(celsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

ingreso_1 = int(input("Ingrese un primer numero: "))
ingreso_2 = int(input("Ingrese un segundo numero: "))
ingreso_3 = int(input("Ingrese un tercero numero: "))

funciones.calcular_promedio(ingreso_1, ingreso_2, ingreso_3)

#--------------------------------------------------------------










