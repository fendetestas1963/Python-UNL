# . Diseñe e implemente un programa en Python en donde se ingrese un número e informe: si es par o impar. si es múltiplo de 5. si es múltiplo de 3. si es múltiplo de 5 y 3 a la vez.
print(" ")
numero = int(input('Ingrese un número: '))
print('usted ingresó el número', numero)
if (numero % 2 == 0) and (numero % 5 == 0) and (numero % 3 == 0):
    print('el número', numero, ' es par, múltiplo de 5 y múltiplo de 3')
elif numero % 2 > 0 and numero % 3 == 0 and numero % 5 > 0:
    print('el número', numero, ' es impar y múltiplo de 3, pero no de 5')
elif numero % 2 > 0 and numero % 3 > 0 and numero % 5 == 0:
    print('el número', numero, ' es impar y múltiplo de 5, pero no de 3')
elif numero%2>0 and numero%5>0 and numero%3>0:
    print('el número', numero, ' no es par y no es múltiplo de 5 ni de 3')
else:
    numero%2 == 0 and numero % 5 > 0 and numero % 3 > 0
    print('el número', numero, ' es par y no es múltiplo de 5 ni de 3')
