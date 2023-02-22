# 5. Escriba un programa en Python donde se ingrese tres números e informe el mayor.

# se pediran 3 numeros diferentes, enteros o no y se compararán sucesitamente para saber cual es el mayor

n1 = float(input("Ingrese el 1er número: "))
n2 = float(input("Ingrese el 2do número: "))
n3 = float(input("Ingrese el 3er número: "))

if (n1 > n2 and n1 > n3):
    print("El primer número ingresado (", n1, ") es el mayor de los tres")
elif (n3 > n2 and n3 > n1):
    print("El tercer número ingresado (", n3, ") es el mayor de los tres")
else:
    (n2 > n1 and n2 > n3)
    print("El segundo número ingresado (", n2, ") es el mayor de los tres")
