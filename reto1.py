#multiplo de 3

numero=int(input("Ingrese un número entero: "))

modulo=numero%3

print(f'El módulo del número {numero} es: {modulo}')

#Condiciones en PYTHON
#if()

if modulo == 0:
    print(f'El número {numero} es múltiplo de 3')
else:
    print(f'El número {numero} NO es múltiplo de 3')

print("fin del programa")
