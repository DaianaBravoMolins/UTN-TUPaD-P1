#Bravo Molins Daiana funciones adicionales

#--------tabla_multiplicar-----------------

# def tabla_multiplicar(x):
#     while x <= 0:
#         print("Debe ser un numero positivo. Reingrese: ")
#         x = int(input("Ingrese un numero positivo: "))

#     if x > 0:
#         print("Tabla: ")

#     for i in range (1,11):
#         calculo = x * i
#         print(f"",x,"*",i,"=",calculo)

#--------suma_pares---------------------------------

def suma_pares(p):
    calculo = 0
    for i in p:
        if i % 2 == 0:
            calculo += i
        suma_total_pares = calculo
    print(suma_total_pares) 

#--------- funcion area y perimetro ------------------

# ▪ Área = longitud * anchura.
# ▪ Perímetro = 2 * (longitud + anchura).

def area_y_perimetro_rectangulo(s,m):
    area = s * m
    perimetro = 2 *(s + m)
    #print(f"El area del perimetro es: ",area,"y su perimetro es: ",perimetro)
    print(area, perimetro)

#---------funcion temperatura--------------------------------

def convertir_temperatura(u):

    farenheit = (u * 9)/5 + 32
    kelvin = u + (273.15)
    print(f"La temperatura es de",kelvin,"° kelvin y",farenheit,"° farenheit.")
    return farenheit, kelvin

