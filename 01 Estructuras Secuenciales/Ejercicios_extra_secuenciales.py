# # Bravo Molins Daiana
# # Ejercicios extra: secuenciales


# # Ejercicio 1: Cálculo del área y el perímetro de un rectángulo
# # Objetivo: Calcular
# # Instrucciones:
# # 1.Pedir al usuario que ingrese el ancho y el alto de un rectángulo.
# # 2.Calcular el área usando la fórmula: ancho * alto.
# # 3.Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2).
# # 4.Mostrar ambos resultados en pantalla.
# # Preguntas de reflexión:
# # •¿Qué sucede si se ingresan valores negativos?
# # •¿Podría adaptarse este cálculo a otras figuras geométricas?


# perimetro_rectangulo = lado + lado + lado + lado + lado 
# area_rectangulo = base * altura

# ancho_rectangulo = int(input("Ingrese el ancho del rectangulo: "))
# alto_rectangulo = int(input("Ingrese el alto del rectangulo: "))

# area = ancho_rectangulo * alto_rectangulo

# perimetro = (ancho_rectangulo * 2) + (alto_rectangulo * 2)

# print(f"El area del rectangulo es:", area,"y su perimetro es:", perimetro)

# # Si se ingresan numeros negativos, de todas formas se hace el calulo (porque no hay validaciones). 
# # Si, pero haciendo mofificaciones por ej el perimetro del restangulo es suma de lados (4 lados), para un
# # triangulo se puede pedir lo mismo pero con 3 cantidades; el romboide y rectangulo tienen la misma formula 
# # para area.
 
# # Ejercicio 2: Conversión de grados Celsius a Fahrenheit
# # Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit.
# # Instrucciones:
# # 1.Solicitar al usuario una temperatura en grados Celsius.
# # 2.Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.
# # 3.Mostrar el resultado en pantalla.
# # Preguntas de reflexión:
# # •¿Qué resultado se obtiene al ingresar 0°C?
# # •¿Cómo se adaptaría este ejercicio para convertir a Kelvin?

# temperatura_celcius = int(input("Ingrese la temperatura en celcius: "))

#conversion_a_Farenheit = (temperatura_celcius * 9/5) + 32

#print(f"El resultado de la conversion a Farenheit es de: ", conversion_a_Farenheit, "grados Farenheit")

# # Se obtienen 32º Farenheit
# # Para Kelvin a los grados celcius se le suma  273.15 grados. 
# # Para Farenheit a kelvin: (x°F − 32) × 5/9 + 273.15 = 385.372 Kelvin

# # Ejercicio 3: Uso de booleanos
# # Objetivo: Manipular variables booleanas y aplicar operadores lógicos.
# # Instrucciones:
# # 1.Declarar dos variables booleanas: a = True, b = False.
# # 2.Realizar e imprimir los resultados de las operaciones:
# # o a and b
# # o a or b
# # onot a, not b
# # Preguntas de reflexión:
# # ¿Cuál es la utilidad de los operadores lógicos en programas más complejos?
# # •¿Qué representa cada operación?

# a = True
# b = False

# print(a and b)  # V and F = False (Falso)
# print(a or b) # V or F = True (verdadero)
# print(a and a) #V and V (Verdadero)

# print(not a, not b) #nor True = False not False = True

# # Permite usarlos como baderas para resolver ejercicios, permite incluir cualquiera de estas dos condiciones dentro
# # de ciclos, condicionales, asignarlos a variables, de esta manera permitiendo que el programa responda de forma
# # diferente de acuerdo al valor boleano asignado. 

# # Ejercicio 4: Prueba de escritorio
# # Objetivo: Analizar el funcionamiento del código y predecir su resultado.
# # Instrucciones:
# # 1.Leer el siguiente código:
# # a = 5
# # b = 3
# # c = a + b
# # a = 2
# # print(c)
# # 2.Realizar una prueba de escritorio paso a paso.
# # 3.Determinar qué imprime el programa y por qué.
# # Preguntas de reflexión:
# # •¿Por qué el cambio en a no afecta al valor de c?
# # •¿Qué pasa si se imprime a y b al final?

# # Linea	a	b	            c	                suma
# # 83	    5	"sin definir"	"sin definir"	"sin definir"
# # 84	    5	3	            "sin definir"	"sin definir"
# # 85	    5	3	            8	                8
# # 86	    2	3	            8	                8
# # 87	    5	3	            8	                8

# # No afecta porque la operacion de suma esa antes de asignarle un nuevo valor a "a".
# # "a" toma el valor de 2, que fue el ultimo valor que se le asigno y "b" imprime el valor 3.

# # Ejercicio 5: Diagrama de flujo – Cuadrado de un número
# # Objetivo: Representar visualmente un algoritmo sencillo.
# # Instrucciones:
# # 1.Dibujar un diagrama de flujo para un programa que:
# # oPide al usuario un número.
# # oCalcula su cuadrado.
# # oMuestra el resultado.
# # 2.Implementar el programa en código si lo deseás.
# # Preguntas de reflexión:
# # •¿Qué ventajas tiene el uso de diagramas de flujo?
# # ¿Cómo se representa una operación matemática en un diagrama?

# # Diagrama:
# # Inicio
# # Pedir datos al usuario
# # calcular el cuadrado del numero que nos otorgaron
# # imprimir por pantalla el resultado
# # Fin

# # Permite persar que se tiene que hacer (la serie de pasos) antes de escribir el codigo. Permite explicarselo a 3ros,
# # detectar errores antes d pasar al codigo y a visualizar la logica.

# # Las operaciones matemáticas (como sumas, restas, multiplicaciones, potencias) se representan dentro de un rectángulo que indica una acción o proceso.

# # Ejercicio 6: Intercambio de variables
# # Objetivo: Intercambiar valores sin usar una variable temporal.
# # Instrucciones:
# # 1.Declarar dos variables: x = 10, y = 20.
# # 2.Intercambiar sus valores usando operaciones aritméticas.
# # 3.Mostrar los valores antes y después del intercambio.
# # Preguntas de reflexión:
# # •¿Cómo funciona el intercambio sin variable auxiliar?
# # •¿Qué pasa si los valores iniciales son iguales?

# x = 10
# y = 20
# print(x,y)

# x = x + y #x = 30
# y = x - y # y = 10
# x = y + y # x = 20
# print(f"nuevo valor de x:",x)

# print(f"nuevo valor de y:",y)

# # Porque el cambio se hace al volver a asignarle otro valor (se usa una operacion matermatica con los valores de las var y su nuevo resultado es el valor que le queda asignado a la variable despues de operar).
# # Si los valores son iguales, despues del intercambio seguiran teniendo el mismo valor.

# # Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal)
# # Objetivo: Aplicar fórmulas con variables numéricas ingresadas por el usuario.
# # Instrucciones:
# # 1.Solicitar al usuario su peso en kg y su altura en metros.
# # 2.Calcular el IMC con la fórmula: IMC = peso / (altura ** 2).
# # 3.Mostrar el resultado con un mensaje como: "Tu IMC es: 22.5".
# # Preguntas de reflexión:
# # •¿Qué rango se considera saludable para el IMC?
# # •¿Cómo podrías dar una recomendación según el resultado?

# peso = float(input("Ingre su peso: "))

# altura = float(input("Ingre su altura: "))

# IMC = peso / (altura ** 2)

# print("Tu IMC es: ",IMC)
# IMC = IMC *100
# print(IMC)

# # Si su IMC es entre 18.5 y 24.9, se encuentra dentro del rango de peso normal o saludable.
# # Si su IMC es menos de 18.5, se encuentra dentro del rango de peso insuficiente. Si su IMC es entre 25.0 y 29.9, se encuentra dentro del rango de sobrepeso.
# # agregaria un condicional en el programa. Al entrar el calculo dentro de alguno de los 2 extremos le indicaria, 
# # 1ro si esta excedido o por debajo del peso normal, de ser asi recomendaria ir a un nutricionista.

# # Ejercicio 8: Contador de caracteres en un nombre
# # Objetivo: Aplicar operaciones con cadenas de texto.
# # Instrucciones:
# # 1.Pedir al usuario que ingrese su nombre completo.
# # 2.Calcular y mostrar:
# # oLa cantidad total de letras (sin contar espacios).
# # oLas primeras 3 letras del nombre.
# # El nombre con letras en mayúsculas y minúsculas alternadas (ejemplo: "JuAn PeReZ").
# # Preguntas de reflexión:
# # •¿Qué técnicas de manipulación de strings estás usando?
# # •¿Cómo podrías extender este ejercicio para apellidos?

nombre = input("Ingrese su nombre completo: ")
extension_nombre = len(nombre.replace(" ",""))  #metodo para descartar espacios 
tres_primeras_letras = nombre[:3] 
letras_alternadas = ""

for i in range(len(nombre)):
    if i % 2 == 0:
        letras_alternadas += nombre[i].upper()
    else:
        letras_alternadas += nombre[i].lower()

print("Su nombre tiene:",extension_nombre, "caracteres, las 3 primeras letras son:",tres_primeras_letras, "y su nombre con mayusculas y minusculas alternadas:",letras_alternadas)

# # Se usan metodos: para contar la cantidad de caracteres del nombre completo (len), otra para que los espacios vacios se descarten y se junten los strings, como si se escribiera sin espacio (replace) 
# # El [] se utilizan tanto para listas como para cadenas de texto (strings). No uso una lista, uso un string entonces la operacion es similar a acceder a elementos en una lista.
# # El programa esta extendido para ser usado con el nombre completo, se uso un for para que itere todo el string
# # y decida por letra si si pone mayuscula o minuscula, y de esta manera se logre alternar entre ambas.

# # Ejercicio 9: Operaciones con números flotantes
# # Objetivo: Realizar distintas operaciones matemáticas con decimales.
# # Instrucciones:
# # 1.Declarar:
# # oa = 7.5
# # ob = 3.2
# # 2.Calcular y mostrar:
# # oLa suma (a + b)
# # oEl redondeo de la división (a / b) a 2 decimales
# # oLa potencia (a ** b)
# # Preguntas de reflexión:
# # •¿Qué ocurre si redondeás a más decimales?
# # •¿Cuándo conviene usar math.pow()?

# a = 7.5
# b = 3.2

# suma = (a+b)
# division_dos_decimales = round(a/b, 2) 
# potencia = (a ** b)
# print(suma, division_dos_decimales, potencia)

# # Deja la cantidad de decimales que le indico, con un resultado mas preciso.
# # math.pow() siempre devuelve un número en punto flotante (float), mientras que ** puede devolver un entero si 
# # ambos operandos son enteros. Es mas preciso.

# # Ejercicio 10: Descuento sobre precio original
# # Objetivo: Aplicar porcentajes y mostrar el resultado.
# # Instrucciones:
# # 1.Pedir al usuario el precio original de un producto.
# # 2.Pedir el porcentaje de descuento.
# # 3.Calcular el precio final: precio_final = precio_original * (1 - (descuento / 100))
# # 4.Mostrar el precio con descuento.
# # 5.(Opcional) Dibujar un diagrama de flujo del proceso.
# # Preguntas de reflexión:
# # •¿Qué ocurre si el descuento es mayor a 100%?
# # •¿Cómo podrías mostrar el monto ahorrado?

# precio_original = int(input("Ingrese el precio del producto:"))
# porcentaje_descuento =  int(input("Ingrese el porcentaje de descuento:"))

# precio_final = precio_original * (1 - (porcentaje_descuento / 100))


# print(precio_final)

# # Inicio
# # pedido de datos para operar (precio y descuento)
# # calculo del precio final
# # Impresion en pantalla del resutlado
# # Fin

# # Si el descuento es mayor a 100 el resultado da negativo. 
# # El monto ahorrado se puede mostrar en una variable que guarde el resultado de restar al precio original el precio final.
