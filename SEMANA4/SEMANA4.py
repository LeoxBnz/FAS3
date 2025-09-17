def ejer1():
    edad = int(input("Ingrese su edad: "))

    if edad < 18:
        print("Menor de edad.")
    else:
        if edad <= 64:
            print("Adulto.")
        else:
            print("Adulto mayor.")

def ejer2():
    an = int(input("Ingrese el año: "))

    if (an % 4 == 0 and an % 100 != 0) or an % 400 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    if (an % 2 == 0):
        print("El año es par")
    else:
        print("El año es impar")

def ejer3():
    monto = float(input("Ingrese monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion = int(input("Ingrese una opcion: "))

    print()
    match opcion:
        case 1: print("Dolares: ", round((monto/3.75),2))
        case 2: print("Euros: ", round((monto/4.05),2))
        case _: print("Opcion incorrecta!")
import math

def ejer4():
    print("Bienvenido al programa de desarrollo de areas\n")

    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("Elija una opcion: "))

    match opcion:
        case 1:
            lado = int(input("Ingrese lado: "))
            print("Area del cuadrado ", lado*lado)
        case 2:
            bse = int(input("Ingrese base: "))
            alt = int(input("Ingrese altura: "))
            print("Area del rectangulo ", bse*alt)
        case 3:
            bse2 = int(input("Ingrese base: "))
            alt2 = int(input("Ingrese altura: "))
            print("Area del triangulo: ", (bse2*alt2)/2)
        case 4:
            rdo = float(input("Ingrese radio: "))
            print("El area del circulo: ", round((math.pi * rdo**2),2))
        case _: print("Opcion incorrecta!")

ejer4()
