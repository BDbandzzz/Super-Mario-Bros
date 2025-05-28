import os

def calculadora(n1,n2,opcion):
    if opcion == 1:
        resultado = n1 + n2
    elif opcion == 2:
        resultado = n1 - n2
    elif opcion == 3:
        resultado = n1 * n2
    elif opcion == 4:
        resultado = n1 // n2
    elif opcion == 5:
        resultado = round(n1 / n2,2)
    
    
    return resultado 


def funcion():
    N1 = int(input("ingrese N1: "))
    N2 = int(input("ingrese N2: "))

    opcion = int(input("Ingrese una opcion entre 1 y 5: "))
    while opcion not in [1,2,3,4,5]:
        print ("Ingrese un numero valido")
        opcion = int(input("Ingrese una opcion entre 1 y 5: "))    
        funcion = calculadora(n1=N1, n2=N2, opcion=opcion) 
        
        
    return print(funcion)
        
        

fuwu = funcion()
uwu = input("Desea hacer otra operacion?:").strip().lower()
while uwu not in ["si","no"]:
    if uwu == "si":
        funcion() 
    else:
        print("Gracias por usar la calculadora :D")
        break
