#Bravo Molins Daiana Mariel Tp Funciones

#---------------- funcion imprimir_hola_mundo----------------
# def imprimir_hola_mundo():
#      print("Hola Mundo!")
#      return

#---------------función saludar_usuario(nombre)--------------
# def saludar_usuario(j):
#     return(f"Hola, {j}!")

#----------------funcion informacion_personal----------------
# def informacion_personal(x, y, z, t):
#     print(f"Soy {x} {y}, tengo {z} años y vivo en {t}")
#     return 

#----------------funcion area y perimetro del circulo---------
# import math
# def calcular_area_circulo(radio):
#     area_circulo = math.pi * (radio * radio)                    #Area = pi * radio al cuadrado
#     return(f"El area del circulo es de: {area_circulo} cm")


# def calcular_perimetro_circulo(radio):
#     perimetro_circulo = 2 * math.pi * radio                     #Perimetro = 2 * pi * radio
#     return (f"El perimetro del circulo es de: {perimetro_circulo} cm")

#---------------------funcion segundos_a_horas----------------

# def segundos_a_horas(segundos):
#     calculo = segundos/60/60
#     return f"La cantidad es de: {calculo} horas."

#----------------------funcion tabla--------------------------

# def tabla(s):
#     for i in range(1,11):
#         calculo = s* i
#         print(s,"*", i,"=",calculo)

#---------------------operaciones_basicas(a, b)----------------

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b
#     tupla_resultados = (suma, resta, multiplicacion, division)
#     print(tupla_resultados)

#------------------calcular_imc(peso, altura)------------------
#El imc se calcula: peso/(altura)elevado al cuadrado

# def calcular_imc (s,r):
#     calculo = s/(r*r)
#     redondeo= round(calculo, 2)
#     print(f"Su indice de masa corporal es de", redondeo)

#--------celsius_a_fahrenheit(celsius)------------------------
#°F = °C x 9 ÷ 5 + 32

def celsius_a_farenheit(z):
    calculo = ((z * 9 )/5 ) + 32
    print(f"La temperatura en grados Fatenheit es de:",calculo,"°")

#----------calcular_promedio(a, b, c)--------------------------

def calcular_promedio(m,n,o):
    calculo = (m + n + o) / 3
    print(f"El promedio de los numeros ingresados es de: ",calculo)

#--------------------------------------------------------------





