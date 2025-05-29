#Funciones - Bravo Molins Daiana

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# #funciones:
# def imprimir_hola_mundo():
#     print("Hola Mundo!")
#     return

# #programa principal:
# imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# #funcion:
# def saludar_usuario(nombre):
#     return(f"Hola, {nombre}!")

# #programa principal:
# saludo = saludar_usuario("Daiana")
# print(saludo)


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

# #Funcion:
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")
#     return 

# #Programa:
# nombre_ingresado = input("Ingrese su nombre: ")
# apellido_ingresado = input("Su apellido: ")
# edad_ingresada = input("Su edad: ")
# residencia_ingresada = input("Su residencia: ")

# informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# import math
# #Funciones:
# def calcular_area_circulo(radio):
#     area_circulo = math.pi * (radio * radio)                    #Area = pi * radio al cuadrado
#     return(f"El area del circulo es de: {area_circulo} cm") 

# def calcular_perimetro_circulo(radio):
#     perimetro_circulo = 2 * math.pi * radio                     #Perimetro = 2 * pi * radio
#     return (f"El perimetro del circulo es de: {perimetro_circulo} cm")
    
# #Programa principal:

# radio = int(input("Ingrese el radio de un circulo: "))
# print(calcular_area_circulo(radio))
# print(calcular_perimetro_circulo(radio))


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

#Funcion:
def segundos_a_horas(segundos):
    calculo = segundos / 60 / 60
    return f"La cantidad es de: {calculo} horas."

#Programa principal:

segundos_ingresados = int(input("Ingrese una cantidad de segundos: "))
print(segundos_a_horas(segundos_ingresados))




# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.











# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.











# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.









# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.





# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.