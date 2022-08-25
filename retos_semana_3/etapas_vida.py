#Calcular la etapa de la vida, según edad:
#-0-14:  niño
#-15-28:  Joven
#-28-60:  Adulto
#>60: Adulto mayor  

edad = int(input("Ingrese su edad: "))

if edad>=0 and edad<=14:
    print(f'Según su edad ({edad} años), se encuentra en la etapa de Niño')
elif edad>=15 and edad <=28:
    print(f'Según su edad ({edad} años), se encuentra en la etapa de Joven')
elif edad>28 and edad <=60:
    print(f'Según su edad ({edad} años), se encuentra en la etapa de Adulto')
elif edad>60:
    print(f'Según su edad ({edad} años), se encuentra en la etapa de Adulto Mayor')
else:
    print("Edad ingresada no es correcta. No ingrese ni números negativos ni letras, solo números enteros.")

