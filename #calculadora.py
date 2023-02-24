#Se requiere implementar una calculadora básica. Para ello, el usuario debe ingresar dos números y luego el sistema deberá mostrar por pantalla el siguiente menú:
#Menú:
#Ingrese + para sumar los números
#Ingrese - para restar los números
#Ingrese * para multiplicar los números
#Ingrese / para calcular la división del primero con el segundo número
#Ingrese P para calcular la potencia del primero elevado al segundo número 
#Nota: Tenga en cuenta que la división por cero no está definida, por lo que deberá informar al usuario con un mensaje alusivo.
print('Esta es la calculadora SuperPython 2023')
print('Solo puede sumar, restar, multiplicar y dividir, pero recuerde que no puede dividir por cero.')
n1=float(input('Ingrese el primer número'))
n2=float(input('Ingrese el segundo número'))

op=int(input('Ingrese 1 para sumar, 2 para restar, 3 para multiplicar y 4 para dividir'))
dec=int(input('Ingrese el número de decimales del resultado'))
if op==1:
    print ('el resultado es :',(n1+n2))
elif op==2:
    print ('el resultado es :',(n1-n2))
elif op==3:
    print ('el resultado es :',(n1*n2))
else:
    op==4
    print ('el resultado es :',round(n1/n2,dec))

