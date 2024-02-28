print ("HELLO WORLD")

#Crea una funcion que pida altura, peso y calcule el IMC
print ("Este programa calcula el IMC")
altura = float(input("Escribe tu altura en m: "))
peso = float(input("Escribe tu peso en kg: "))

def IMC(h,m):
    IMC_persona = m/(h*h)
    if IMC_persona <= 18.5:
        print("Tienes un peso bajo para tu altura")
    if IMC_persona <= 24.9:
        print("Tienes un peso saludable")
    if IMC_persona <= 29.9:
        print("Con sobrepeso")
    if IMC_persona <= 39.9:
        print("Obeso")
    else :
        print("Estas muy gordo")

IMC(altura,peso)