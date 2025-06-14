#Bravo Molins Daiana - Ejercicio de funciones adicionales- Programa principal

import funciones_adicionales

# Ejercicio 1: Tabla de multiplicar
# Objetivo: Generar una tabla de multiplicar usando funciones. Instrucciones:
# 1.Crea una función tabla_multiplicar que reciba un número entero positivo.
# 2.Devuelve una lista con su tabla de multiplicar del 1 al 10.
# oEjemplo: Para 3 → [3, 6, 9, ..., 30].
# Preguntas de reflexión:
# •¿Cómo adaptarías la función para recibir el rango (ej: hasta 12)?
# •¿Qué ocurre si se ingresa un número negativo?

# numero_ingresado = int(input("Ingrese un numero positivo: "))

# funciones_adicionales.tabla_multiplicar(numero_ingresado)

#modificaria el range: (1,13) para que el iterador llegue a multiplicar por 12.
#Se restringe el ingreso con un while pidiendo siempre un ingreso positivo.

# Ejercicio 2: Suma de números pares
# Objetivo: Sumar elementos pares de una lista con una función. Instrucciones:
# 1.Define una función suma_pares que reciba una lista de enteros.
# 2.Retorna la suma de los números pares.
# o Ejemplo: Para [1, 2, 3, 4, 5, 6] → 12.
# Preguntas de reflexión:
# •¿Cómo manejarías listas vacías o con decimales?
# •¿Qué ventaja tiene usar una función en lugar de código inline?

# lista_enteros = [3,7,2,8,2,1]

# funciones_adicionales.suma_pares(lista_enteros)

#Si tuviera la lista vacia, pediria el ingreso por parte del usuario en una nueva variable.
# Luego usaria un .append() para ir haciendo ingresos. Una vez finalizada, llamaria a la funcion. Asi: 
 
# lista_vacia =[]

# ingreso = int(input("Ingrese: "))
# ingreso_2 =  int(input("Ingrese: "))
# lista_vacia.append(ingreso)
# lista_vacia.append(ingreso_2)

# print(lista_vacia)

#Una de las ventajas es que todo se anota adentro de la funcion, luego en el programa principal yo no repito lo que quiero que haga el codigo sino que lo reutilizo haciendo llamadas a la funciones (las veces que lo necesite), cambiandole los argumentos, y operando de la misma manera con datos diferentes. En lugar de repetir codigo en el programa principal para cambiar los datos. 
# queda mas organizado el codigo. Sin algo no funciona en la funcion, voy dentro de ella y modifico esa parte. Entonces es facil encontrar en cual de todas mis funciones se encuentra el error.

# Ejercicio 3: Área y perímetro de un rectángulo
# Objetivo: Calcular múltiples valores en una función. Instrucciones:
# 1.Crea una función rectángulo que reciba longitud y anchura
# 2.Retorna una tupla con el área y el perímetro.
# o Fórmulas:
# ▪ Área = longitud * anchura.
# ▪ Perímetro = 2 * (longitud + anchura).
# Preguntas de reflexión:
# • ¿Por qué usar una tupla en lugar de una lista?
# •¿Cómo validarías que las dimensiones sean positivas?

# longitud_rectangulo = float(input("Ingrese la longitud del rectangulo: "))
# anchura_rectangulo = float(input("Ingrese la anchura del rectangulo: "))

# funciones_adicionales.area_y_perimetro_rectangulo(longitud_rectangulo,anchura_rectangulo)

#Porque no se pide lista, y como son dos valores los calculados, los mostrados como tupla.
#Con un while que mientras el usuario ingrese numeros menores o iguales a cero, me pida un reingreso.

# Ejercicio 4: Conversión de temperatura
# Objetivo: Convertir temperaturas con condiciones. Instrucciones:
# 1. Define una función convertir_temperatura que reciba:
# o Temperatura en Celsius.
# o Unidad de destino ("F" o "K").
# 2.Retorna la temperatura convertida usando:
# oFahrenheit: F = C * 9/5 + 32.
# oKelvin: K = C + 273.15.
# Preguntas de reflexión:
# •¿Qué pasa si se ingresa una unidad no válida?
# •¿Cómo extenderías la función para convertir entre otras unidades?
temperatura = float(input("ingrese una temperatura en grados centigrados: "))

funciones_adicionales.convertir_temperatura(temperatura)

#Puedo agregar un while que no tome determinados rangos de numeros para temperaturas y/o tambien que no tome strings.
#Agregaria mas variables locales dentro de la funcion consus respectivos calculos e igual cantidad de parametros y argumentos.
      
# Ejercicio 5: Verificador de números primos
# Objetivo: Implementar una función para detectar primos. Instrucciones:
# 1.Crea una función es_primo que reciba un entero positivo.
# 2.Retorna True si es primo (solo divisible por 1 y sí mismo), False en caso contrario.
# oEjemplo: 7 → True, 8 → False.
# Preguntas de reflexión:
# •¿Cómo optimizarías la función para números grandes?
# •¿Qué estructura de control es más eficiente aquí: for o while?





#Un while es mas eficiente. 



# Ejercicio 6: Promedio de calificaciones
# Objetivo: Calcular promedios con funciones. Instrucciones:
# 1.Define una función promedio_calificaciones que reciba una lista de notas (0 a 10).
# 2.Retorna el promedio. Si la lista está vacía, retorna 0.
# o Ejemplo: [8.5, 9.0, 7.5, 8.0] → 8.25.
# Preguntas de reflexión:
# •¿Cómo manejarías notas fuera del rango 0-10?
# •¿Qué ventaja tiene retornar 0 en lugar de None para listas vacías?





# Ejercicio 7: Factorial con validación
# Objetivo: Combinar funciones para validar y calcular. Instrucciones:
# 1.Usa dos funciones:
# ovalidar_entrada: Verifica si un número es entero no negativo.
# o factorial: Calcula el factorial (ej: 5! = 120).
# 2.El programa principal debe:
# oPedir un número al usuario.
# oValidarlo y mostrar el factorial o un error.
# Preguntas de reflexión:
# •¿Por qué separar la validación del cálculo?
# •¿Cómo manejarías el desbordamiento para números grandes?



# Ejercicio 8: Números primos con funciones auxiliares
# Objetivo: Modularizar la lógica de primos. Instrucciones:
# 1.
# Usa dos funciones:
# o
# es_divisible: Retorna True si un número divide a otro.
# o
# es_primo: Usa es_divisible para verificar si es primo.
# 2.
# El programa principal pide un número y muestra si es primo.
# Preguntas de reflexión:
# •
# ¿Cómo reutilizarías es_divisible en otros contextos?
# •
# ¿Qué optimizaciones aplicarías a es_primo?
# Ejercicio 9: Conversor de temperatura con menú
# Objetivo: Integrar funciones con interacción de usuario. Instrucciones:
# 1.
# Usa tres funciones:
# o
# convertir_a_fahrenheit: Convierte Celsius a Fahrenheit.
# o
# convertir_a_kelvin: Convierte Celsius a Kelvin.
# o
# menu_conversion: Muestra un menú para elegir la unidad.
# 2.
# El programa principal:
# o
# Pide la temperatura en Celsius.
# o
# Muestra el resultado según la unidad elegida.
# Preguntas de reflexión:
# ¿Cómo mejorarías la experiencia de usuario del menú?
# •
# ¿Qué pasa si el usuario ingresa una opción inválida?
# Ejercicio 10: Rectángulo con validación
# Objetivo: Validar entradas antes de calcular. Instrucciones:
# 1.
# Usa tres funciones:
# o
# validar_dimensiones: Verifica que longitud y anchura sean positivas.
# o
# calcular_area: Retorna el área del rectángulo.
# o
# calcular_perimetro: Retorna el perímetro.
# 2.
# El programa principal:
# o
# Pide las dimensiones al usuario.
# o
# Valida y muestra resultados o un error.
# Preguntas de reflexión:
# •
# ¿Por qué es importante validar las entradas?
# •
# ¿Cómo extenderías el programa para otras figuras geométricas?
# Bonus:
# •
# Pruebas: Escribe casos de prueba para cada función.
