#Ejercicios de python

""" 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un 
     muy buen ejercicio.
"""
"""
print("Este programa te regresara el numero más grande de 2 ")

num1 = input("Ingresa el primer número:  ")
num2 = input("Ingresa el segundo número:  ")

def funcion_max(n1,n2):
    if n1>n2:
        print("El número mayor es: ", n1)
    else:
        print("El número mayor es ", n2)


funcion_max(num1,num2)

"""
"""2 - Definir una función max_de_tres(), que tome tres números como argumentos y 
devuelva el mayor de ellos.
"""
def max_de_3(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
    
print(max_de_3(-2,100,1550))



