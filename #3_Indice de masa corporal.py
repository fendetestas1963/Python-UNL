# 3. Diseñe e implemente un programa en Python que calcule el Índice de masa corporal (IMC) de una persona a partir del peso y altura ingresados por un usuario. Informar la condición del usuario a partir de los valores obtenidos de IMC según la siguiente tabla:
# peso/altura
peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros: '))
IMC = peso/altura**2
IMC = round(IMC, 1)
if IMC < 18.5:
    print('Su IMC es ', IMC, 'e indica que tiene bajo peso')
elif IMC >= 18.5 and IMC <= 24.9:
    print('Su IMC es ', IMC, ' e indica que tiene un peso normal')
elif IMC >= 25 and IMC <= 29.9:
    print('Su IMC es ', IMC, ' e indica que tiene un sobrepeso')
elif IMC >= 30 and IMC <= 34.9:
    print('Su IMC es ', IMC, ' e indica que obesidad tipo 1')
elif IMC >= 35 and IMC <= 39.9:
    print('Su IMC es ', IMC, ' e indica que obesidad tipo 2')
else:
    IMC >= 40
    print('Su IMC es ', IMC, ' e indica que obesidad tipo 3')
