#4. Deseamos saber si un estudiante de colegio secundario vota en las próximas elecciones legislativas a llevarse a cabo el próximo 24 de octubre, para ello debe ser mayor de 16  años. Escriba un programa en Python donde se ingrese la fecha de nacimiento del estudiante con formato numérico día, mes, año y se informe si vota o no.

anio = int(input('Ingrese el anio de nacimiento en formato "aaaa": '))
mes = int(input('Ingrese el mes de nacimiento: '))
dia = int(input('Ingrese el día de nacimiento: '))


if (anio+16) <= 2023:
    print('El ciudadano puede votar')
elif (anio+15 >= 2023) and mes < 10:
    print('El ciudadano puede votar')
else:
    ((anio+16)==2023) and (mes == 10) and (dia <= 24)
    print('El ciudadano puede votar')
    
