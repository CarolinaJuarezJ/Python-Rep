# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:50:36 2024

@author: carol
"""
#Seguimos con los ejercicios de python de la pagina 
#https://unipython.com/preguntas-de-entrevista-o-examen-sobre-lenguaje-python/
"""
66. Escribe un programa en Python para producir un triángulo de estrellas.
"""

def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))
        #Recuerda que 2x + 1 te da los numeros impares y x empieza en 0 y termina en r-1

pyfunc(9)

#Haz una funcion que cuente del 1 al 10

def counterr(m):
    for x in range (m):
        print(x+1)
        
counterr(10)

#67. Escribe un programa para producir la serie Fibonacci en Python.
"""La serie de Fibonacci empieza con 0 y 1 sumando 2 numeros consecutivos
Ejemplo: 0 1 1 2 3 5 8 13 21 """

"""a = int(input("Ingresa el número de terminos que requieras en la serie de fibonacci"))

f = 0       #Primer número
s = 1       #Segundo número

def fibonacci(x):
    if x<=0:
        print("Las series requeridas son ",f)
"""
def a(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()

a(4)

print("Este es otro ejercicio")

def rect(h,b):
    for i in range(h):
        for j in range(b):
            if i == 0 or i == h-1 or j == 0 or j == b-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()

rect(3,6)    
print("¿y si quiero el recangulo lleno?")

def rect_completo(h,b):
    for i in range(h):
        print("*"*b)
        
rect_completo(3,6)

