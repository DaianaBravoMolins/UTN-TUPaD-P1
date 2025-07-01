# #Bravo Molins Daiana Mariel
# #Datos complejos

# # 1) Dado el diccionario precios_frutas
# # precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# # Añadir las siguientes frutas con sus respectivos precios:
# # ● Naranja = 1200
# # ● Manzana = 1500
# # ● Pera = 2300

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# print(precios_frutas)
# precios_frutas.update({'Naranja': 1200,'Manzana': 1500,'Pera':2300})

# print(precios_frutas)

# #2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# # ● Banana = 1330
# # ● Manzana = 1700
# # ● Melón = 2800


# precios_frutas['Banana'],precios_frutas['Manzana'],precios_frutas['Melón'] = 1330, 1700, 2800
# print(precios_frutas)

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
# lista_frutas = []
# print(precios_frutas.keys())

# lista_frutas = list(precios_frutas.keys())
# print(lista_frutas)

# # 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# # • Luego, pedí un nombre y mostrale el número asociado, si existe.
# miscontactos = {}

# for contacto in range(5):
#     contacto_ingresado = input("Ingrese el nombre del nuevo contanto: " )
#     telefono_ingresado = int(input("Ingrese su numero: " ))
#     miscontactos.update({contacto_ingresado: telefono_ingresado})

# print(miscontactos)

# contacto_buscado = input("Ingrese el nombre del contacto que busca: ")

# if contacto_buscado in miscontactos:
#     print(miscontactos[contacto_buscado])
# else:
#     print("Contacto inexistente.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# frase_ingresada = input("Por favor, ingrese una frase: ")

# lista_palabras_separadas = frase_ingresada.split()

# set_de_la_frase = set(frase_ingresada.split())
# print(set_de_la_frase)

# diccionario_frase = {}

# for palabra in lista_palabras_separadas:
#     if palabra not in diccionario_frase:
#         diccionario_frase[palabra] = 1
#     else:
#         diccionario_frase[palabra] += 1
        
        
# print(diccionario_frase)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.  
