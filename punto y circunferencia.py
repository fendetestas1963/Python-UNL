#Escriba un programa que pida el radio, las coordenadas del centro de una circunferencia y las coordenadas de un punto y que indique si el punto está sobre la circunferencia, dentro o fuera de ella.
#Se recuerda que un punto está fuera, dentro o sobre la circunferencia según sea la relación entre el radio y la distancia entre el punto y el centro de la circunferencia.
#La distancia entre dos puntos A(x, y) y B(x, y) se calcula mediante la fórmula: 
# d(a.b)={(Xb-Xa)**2+(Yb-Ya)**2}**0.5

rad=float(input('Ingrese el radio de la circunferencia: \n'))
Xa=float(input('Ingrese la coordenada a del punto X: \n'))
Xb=float(input('Ingrese la coordenada b del punto X: \n'))
Ya = float(input('Ingrese la coordenada a del punto Y: \n'))
Yb = float(input('Ingrese la coordenada b del punto Y: \n'))
dis=((Xb-Xa)**2+(Yb-Ya)**2)**0.5
if dis>rad:
    print('El punto está fuera de la circunferencia')
elif dis<rad:
    print('El punto está dentro de la circunferencia')
else : 
    dis==rad
    print('El punto está sobre de la circunferencia')