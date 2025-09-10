def ejer1():
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")

    print(f"\n{nombre}, bienvenido a FA de {carrera}")

def ejer2():
    print("\"Leonardo\"")

def ejer3():
    num1 = int(input("Ingrese numero 1: ")):
    num2 = int(input("Ingrese numero 1: ")):

    print("\nSuma: ", (num1+num2));
    print("Resta: ", (num1-num2));
    print("Multiplicacion: ", (num1*num2));
    print("Division: ", divi);

import  math #importando la libreria math

def ejer4():
    num = float(input("Ingrese un numero decimal: "))

    raiz2 = math.sqrt(num)
    redo = round(num,0)
    cubo = math.pow(num,3)
    raiz3 = math.pow(num,1/3)

    print("\nRaiz 2: ", raiz2)
    print("Redondeado: ", redo)
    print("Al cubo: ", cubo)
    print("Raiz 3: ", raiz3)

def ejer5():
    num = input("Ingrese un numero: ")

    entero = int(num)
    deci = float(num)

    print("\nResto: ", entero%2)
    print("Dividido: ", deci/3)

ejer5()