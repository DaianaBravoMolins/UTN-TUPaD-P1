# #Bravo Molins 
# #Estructuras condicionales

# # Ejercicio 1: Validación de contraseña
# # Objetivo: Analizar un programa existente que verifica una contraseña. Instrucciones:
# # 1.Lee el siguiente código y explica qué hace:
# # contrasena_correcta = "programacion1"
# # contrasena_usuario = input("Introduce la contraseña: ")
# # if contrasena_usuario == contrasena_correcta:
# #     print("Contraseña correcta. Bienvenido.")
# # else:
# #     print("Contraseña incorrecta. Intenta de nuevo.")
# # Preguntas de reflexión:
# # •¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
# # •¿Cómo mejorarías el programa para dar más intentos?

# #Si se anota en mayusculas no reconoce la contraseña.
# # Para permitir 3 intentos se puede poner un ciclo con un contador. Si el 3er intento es erroneo se sale del programa. O con varios if-else anidados.Asi:

# contrasena_correcta = "programacion1"
# contrasena_usuario = input("Introduce la contraseña: ") #1er intento

# if contrasena_usuario == contrasena_correcta:  
#     print("Contraseña correcta. Bienvenido.")
# elif contrasena_usuario != contrasena_correcta: 
#     print("Contraseña incorrecta. Intenta de nuevo (2do intento)")  #2do intento
#     contrasena_usuario = input("Introduce la contraseña: ")
#     if contrasena_usuario == contrasena_correcta: 
#         print("Contraseña correcta. Bienvenido.")
#     elif contrasena_usuario != contrasena_correcta:
#         print("Contraseña incorrecta. Intenta de nuevo (ultimo intento): ") #3er intento
#         contrasena_usuario = input("Introduce la contraseña: ")
#         if contrasena_usuario == contrasena_correcta:
#             print("Contraseña correcta. Bienvenido.")
#         else:
#             print("bloqueado.")

# # Ejercicio 2: Identificador de vocales
# # Objetivo: Clasificar caracteres usando condicionales. Instrucciones:
# # 1.Solicita una letra al usuario.
# # 2.Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra ingresada es una vocal".
# # 3.En otro caso, imprime: "La letra ingresada no es una vocal".
# # Preguntas de reflexión:
# # • ¿Cómo manejarías vocales acentuadas (á, é)?
# # • ¿Qué estructura usarías para simplificar las comparaciones?

# letra = input("Ingrese una letra: ")

# if letra == "á" or letra == "e" or letra == "i" or letra == "o" or letra == "u": 
#     print("La letra ingresada es una vocal")
# else:
#     print("La letra ingresada no es una vocal")

# #Agrego como otras opciones las vocales con sus respectivas tildes, para que tambien las tome como vocales-
# #se puede crear un ciclo for vocal in range(letra) o tambien un  if letra in "aeiouáéíóú" para anotar todo junto y que lo busque ahi.


# # Ejercicio 3: Clasificador de números
# # Objetivo: Determinar el signo de un número. Instrucciones:
# # 1. Pide un número al usuario.
# # 2. Si es positivo, imprime: "El número es positivo".
# # 3.Si es negativo, imprime: "El número es negativo".
# # 4.Si es cero, imprime: "El número es cero".
# # Preguntas de reflexión:
# # •¿Qué ocurre si el usuario ingresa un texto?
# # •¿Cómo adaptarías el código para números decimales?


# numero = int(input("Ingrese un numero: "))

# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# else:
#     print("El número es cero")

# #Si ingreso un string se interrumpe la ejecucion del codigo.
# #En lugar de int usaria un float para operar con numeros decimales.

# # Ejercicio 4: Comparador de números
# # Objetivo: Comparar dos números con condicionales. Instrucciones:
# # 1.Solicita dos números al usuario.
# # 2.Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# # 3.Si el primero es menor, imprime: "El primer número ingresado es menor".
# # 4.Si son iguales, imprime: "Los números ingresados son iguales".
# # Preguntas de reflexión:
# # •¿Cómo modificarías el programa para comparar más de dos números?
# # •¿Qué pasa si se ingresan valores no numéricos?

# primer_numero = int(input("Ingrese un primer numero: "))
# segundo_numero = int(input("Ingrese un segundo numero: "))

# bandera_menor = float("Inf")
# bandera_mayor = float("-inf")

# if primer_numero > segundo_numero:
#     print("El primer número ingresado es mayor")
# elif primer_numero < segundo_numero:
#     print("El primer número ingresado es menor")
# else:
#     print("Los números ingresados son iguales.")

# #Inicializo una tercer variable y agrego en el condicional if operadores logicos para comparar (and por ej para comprobar que el 1° es mas grande que el 2° y que el 1° es mas grande que el 3°). 


# # Ejercicio 5: Clima según temperatura
# # Objetivo: Clasificar temperaturas en rangos. Instrucciones:
# # 1.Pide la temperatura actual en °C.
# # 2.Si es ≤ 10°C, imprime: "Hace frío".
# # 3.Si está entre 10°C y 25°C, imprime: "Está templado".
# # 4.Si es > 25°C, imprime: "Hace calor".
# # Preguntas de reflexión:
# # •¿Cómo adaptarías el programa para usar °F?
# # •¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?

# temperatura_Actual = float(input("Ingrese la temperatura: "))

# if temperatura_Actual <= 10:
#     print("Hace frio.")
# elif 10 < temperatura_Actual < 25:
#     print("Esta templado.")
# else:
#     print("Hace calor.")

# #Agregaria en un renglon entre la varible y el if una linea de codigo donde agrego el calulo para temperatura Farenheit.
# #"La temperatura esta por debajo de cero,a briguese." "La temperatura es demasiado alta, permanezca en la casa e hidratese."

# # Ejercicio 6: Detector de años bisiestos
# # Objetivo: Aplicar condiciones compuestas. Instrucciones:
# # 1.Pide un año al usuario.
# # 2.Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se ingresó un año bisiesto".
# # 3.En otro caso, imprime: "Se ingresó un año no bisiesto".
# # Preguntas de reflexión:
# # •¿Por qué el año 1900 no es bisiesto?
# # •¿Cómo validarías que el año sea positivo?

# anio = int(input("Ingrese un año: "))

# if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#     print("Se ingreso un año bisiesto.")
# else:
#     print("Se ingreso un año no bisiesto.")

# #porque 1900 no es divisible por 400. Si es divisible por 4 pero tambien lo es por 100 (para serlo deberia no ser divisible por 100).
# #Pondria un primer "If" que me pida que el año sea mayor a cero.

# # Ejercicio 7: Ajustador de frases
# # Objetivo: Manipular strings con condicionales. Instrucciones:
# # 1.Pide una frase o palabra al usuario.
# # 2. Si no termina en punto, añádelo al final.
# # 3.Imprime el resultado.
# # Preguntas de reflexión:
# # •¿Cómo manejarías frases que terminan con espacios?
# # •¿Qué otros caracteres de puntuación podrías considerar?

# frase = input("Ingrese una frase por favor: ")

# if frase[-1] != ".":
#     print(frase + ".")

# #agregaria en el "if" otra condicion que si temina con espacio le agregue un punto. if frase[-1] == " " que le agregue el punto.
# #Exclamacion, interrogacion, punto y coma, dos puntos, coma.


# # Ejercicio 8: Validador de contraseña segura
# # Objetivo: Implementar múltiples condiciones. Instrucciones:
# # 1.Pide al usuario que cree una contraseña.
# # 2.Verifica que cumpla:
# # o 8+ caracteres y ≤20 caracteres.
# # o Al menos 1 mayúscula (usa .isupper()).
# # o Al menos 1 número (usa .isdigit()).
# # 3.Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
# # 4.Si no, imprime: "La contraseña no es segura.".
# # Preguntas de reflexión:
# # •¿Cómo añadirías la regla de usar un carácter especial?
# # # •¿Por qué es importante limitar la longitud máxima?

# contrasenia = input("Ingrese una contraseña: ")
# largo_contrasenia = len(contrasenia)
# contador_letra = 0
# contador_numero = 0

# if 8 <= largo_contrasenia <= 20: 
#     for letra in contrasenia:
#         if letra.isupper():
#             contador_letra += 1
#         if letra.isdigit():
#             contador_numero += 1
#     if contador_letra == 0:
#         print("Debe anotar al menos una letra mayuscula.")
#     if contador_numero == 0:
#         print("Debe anotar al menos un numero.")
#     else:
#         print("¡Felicitaciones! Creaste tu contraseña.")
# else:
#     print("La contraseña no es segura.") 

# #Puedo verificar si hay numero con isdigit o letras con isalpha. Sino no es nunguna de las dos, es porque hay simbolos.
# #Porque es mas facil para verificar, si es demasiado larga se puede confundir el usuario al anotarla o se la puede olvidar. Y para no consumir tanto espacio de memoria.

# # Ejercicio 9: Mejorando mensajes de error
# # Objetivo: Dar retroalimentación específica al usuario. Instrucciones:
# # 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# # o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al menos 8 caracteres.".
# # o Si tiene >20 caracteres: "...no más de 20 caracteres.".
# # o Si falta mayúscula: "...al menos una mayúscula.".
# # o Si falta número: "...al menos un número.".
# # Preguntas de reflexión:
# # • ¿Cómo evitarías repetir código al verificar cada condición?
# # •¿Qué ventajas tiene este enfoque para el usuario?

# contrasenia = input("Ingrese una contraseña: ")
# largo_contrasenia = len(contrasenia)
# contador_letra = 0
# contador_numero = 0

# if largo_contrasenia < 8:
#     print("La contraseña no es segura. Debe tener al menos 8 caracteres")
# if largo_contrasenia > 20:
#     print("...no más de 20 caracteres.")
#     for letra in contrasenia:
#         if letra.isupper():
#             contador_letra += 1
#         if letra.isdigit():
#             contador_numero += 1
#     if contador_letra == 0:
#         print("...al menos una mayúscula.")
#     if contador_numero == 0:
#         print("...al menos un número.")
#     else:
#         print("¡Felicitaciones! Creaste tu contraseña.")
# else:
#     print("La contraseña no es segura.") 

#La manera de no repetir es usando ciclos: for o while. Sino queda un codigo demasiado largo, al no poder usar ciclo hay que verificar letra por letra si hay mayuscula en caso de que sean 20 caracteres, verificar lo mismo, en caso de que se anoten 19 caracteres... hasta llegar a uno. lo mismo para numero: verificar caracter por caracter si hay numero cuando la contraseña es de 20 caracteres, cuando es de 19, de 18, etc.
#Que por cada error que comete, le aparece un mensaje indicandole en que se equivoco.

# # Ejercicio 10: Piedra, papel o tijera
# # Objetivo: Implementar lógica de juego con condicionales anidados. Instrucciones:
# # 1.Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
# # 2.Usa la tabla proporcionada para determinar el resultado (ganador o empate).
# # 3.Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE".
# # Preguntas de reflexión:
# # •¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
# # •¿Qué estructura usarías para simplificar las comparaciones?
# # Bonus:
# # • Diagrama de flujo: Dibuja el diagrama de flujo del Ejercicio 10.

entrada_jugador_1 = input("Haga su ingreso: ")

entrada_jugador_2 = input("Haga su ingreso: ")

if (entrada_jugador_1 == "Piedra" and entrada_jugador_2 == "Piedra") or (entrada_jugador_1 == "Papel" and entrada_jugador_2 == "Papel") or (entrada_jugador_1 == "Tijera" and entrada_jugador_2 == "Tijera"):
    print("Empate")
elif (entrada_jugador_1 == "Piedra" and entrada_jugador_2 == "Tijera") or (entrada_jugador_1 == "Papel" and entrada_jugador_2 == "Piedra") or (entrada_jugador_1 == "Tijera" and entrada_jugador_2 == "Papel"):
    print("Gana jugador 1")
else: 
    print("Gana jugador 2")

#Podria un while que no me deje continuar hasta haber escrito la palabra de forma correcta y de ahi se comiencen las comparaciones.
#Para el empate podria haber comparado directamente las respuestas del ambos jugadores, sin necesidad de decir si es piedra, papel o tijera. 

#Diagrama:
#Inicio programa
# ingreso 1º jugador
# ingreso 2º jugador
# Comparacion
# 2 respuestas iguales  o  eleccion + fuerte 1º jugador  o   eleccion + fuerte 2º jugador 
# Empate                      Gana jugador 1º                      Gana 2º jugador
# Fin                         



