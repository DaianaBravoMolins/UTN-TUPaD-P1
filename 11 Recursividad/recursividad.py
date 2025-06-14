#Bravo Molins Daiana - Recursividad. 
# Funciones


def factorial_recursivo(num):
    if num == 0:
        return 1 
    else:
        return num * factorial_recursivo(num-1)
    

def calculo_factorial_recursivo (s):
    if s == 0:
        return 1 
    else:
        return s * factorial_recursivo(s-1)

#----------------------------------------------------

def fibonacci_recursividad(o):

    if o == 0:
        return 0
    elif o == 1:
        return 1 
    else:
        return fibonacci_recursividad(o-1) + fibonacci_recursividad(o-2) 

#-----------------------------------------
#𝑛𝑚= 𝑛∗𝑛(𝑚−1)

def potencia_recursiva(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia_recursiva(n , m-1 )

#------------------------------------------

def binario_recursivo(k):
    if k == 0:
        return "0"
    elif k == 1:
        return "1"
    else:
        return binario_recursivo(k // 2) + str(k % 2)

#-------------------------------------------------------

def es_palindromo_recursivo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo_recursivo(palabra[1:-1])
    
#--------------------------------------------------

def suma_digito_recursiva(n):
    if n < 10:
        return n 
    else:
        return (n % 10) + suma_digito_recursiva(n // 10)
#-----------------------------------------------------

def  contar_bloques_recursivo(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques_recursivo(n-1)

#----------------------------------------------------

def contar_digito_recursivo(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito_recursivo(numero // 10, digito)
    
    #--------------------------------------------------------------------------