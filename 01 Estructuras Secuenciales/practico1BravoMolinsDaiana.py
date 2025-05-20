#Practico 1: Estructuras secuenciales.
#Bravo Molins Daiana Mariel

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")      #Otra opccion print("Hola " + nombre + "!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese por favor, su nombre: ")
apellido = input("Su apellido: ")
edad = input("Tambien, su edad: ")
lugarResidencia = input("Y por ultimo su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}.")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = int(input("Ingrese el radio de un de un circulo: "))
#formula perimetro = 2.r.π

import math  #importo math de la libreria de python para tener un valor mas aproximado que 3.14

perimetro = 2 * radio * math.pi 

#formula del area del circulo = pi. radio al cuadrado

area = math.pi * (radio * radio)

print(f"El perimetro de un circulo es: {perimetro} y su area es: {area}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

cantidadSegundos = int(input("Por favor, ingrese una cantidad de segundos: "))
# 1 minuto tiene 60 segundos, 1 hora tiene 3600 segundos (60 * 60)
calculo = cantidadSegundos / 3600 

print(f"El valor ingresado corresponde a {calculo} de horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Por favor, ingrese un numero: "))

por1 = 1*numero
por2 = 2*numero
por3 = 3*numero
por4 = 4*numero
por5 = 5*numero
por6 = 6*numero
por7 = 7*numero
por8 = 8*numero
por9 = 9*numero
por10 = 10*numero

print(f"La tabla del numero ingresado es:\n 1 x {numero} = {por1}, \n 2 x {numero} = {por2}, \n 3 x {numero} = {por3}, \n 4 x {numero} = {por4}, \n 5 x {numero} = {por5}, \n 6 x {numero} = {por6}, \n 7 x {numero} = {por7}, \n 8 x {numero} = {por8}, \n 9 x {numero} = {por9}, \n 10 x {numero} = {por10}")

# # #7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# # #pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = float(input("Por favor ingrese un numero distinto de cero: "))


while(numero1 == 0):
    print = input("El numero elegido debe ser diferente de cero.")
    numero1 = float(input("Intentelo de nuevo: "))

numero2 = float(input("Por favor ingrese un segundo numero distinto de cero: "))

while(numero2 == 0):
    print = input("El numero elegido debe ser diferente de cero.")
    numero2 = float(input("Intentelo de nuevo: "))



suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"El resultado de la suma es: {suma}, de la division {division}, de la multiplicacion {multiplicacion} y de la resta es: {resta}.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#    (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2


altura = float(input("Por favor, ingrese su altura: ")) 

peso = float(input("Tambien su peso: "))

indiceMasaCorporal = peso /(altura * altura)

print(f"Su indice de masa corporal es de {indiceMasaCorporal}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperaturaCelsius = float(input("Por favor, ingrese una temperatura: "))

calculoFarenheit = (9/5) * temperaturaCelsius + 32

print(F"La temperatura en grados Farenheit es de: {calculoFarenheit}")


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números

numero1 = float(input("Por favor, ingrese un primer numero: "))
numero2 = float(input("Por favor, ingrese un segundo numero: "))
numero3 = float(input("Por favor, ingrese un tercer numero: "))

calculoPromedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los numeros ingresados es: {calculoPromedio}.")
