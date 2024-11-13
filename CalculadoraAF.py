#Calcular áreas de fíguras
import math

while True:
    print("Escoja el número correspondiente a la fígura que desea que desea calcular ")
    figura = (input("Cuadrado [1], Rectángulo [2], Triángulo [3], Círculo [4] : "))

    if figura == "salir":
        break

    elif figura == "1":
        print("Ingrese las dimensiones a calcular:")
        dimension = float(input("Lado: "))
        area_triangulo = dimension ** 2 
        print(f"El área del triángulo es {area_triangulo} cm²")

    elif figura == "2":
        print("Ingrese las dimensiones a calcular:")
        largo = float(input("largo:  "))
        ancho = float(input("ancho: "))
        area_rectangulo = largo * ancho
        print(f"El área del rectángulo es {area_rectangulo} cm²")

    elif figura == "3":
        print("Ingrese las dimensiones a calcular:")
        base = float(input("base: "))
        altura = float(input("altura: "))
        area_triangulo = (base * altura) /2
        print(f"El área del triángulo es {area_triangulo} cm²")
    
    elif figura == "4":
        radio = float(input("radio: "))
        area_circulo = (radio ** 2) * math.pi 
        print(f"El área del círculo es {area_circulo} cm²")

    else :
        print("respuesta no válida")