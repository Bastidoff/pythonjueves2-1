#Enero, febrero y marozo: invierno
#abril, mayo y junio: primavera
#julio, agosto, septiembre: verano
#octubre. noviembre, diciembre: otoño

mes = input("Digite el mes del año: ")


if mes=="Enero" or mes=="enero" or mes=="febrero" or mes=="Febrero" or mes=="marzo" or mes=="Marzo":
    print(f'La estación del mes {mes} es Invierno')
elif mes=="Abril" or mes=="abril" or mes=="Mayo" or mes=="mayo" or mes=="Junio" or mes=="junio":
    print(f'La estación del mes {mes} es Primavera')
elif mes=="Julio" or mes=="julio" or mes=="Agosto" or mes=="agosto" or mes=="Septiembre" or mes=="septiembre":
    print(f'La estación del mes {mes} es Verano')
elif mes=="Octubre" or mes=="octubre" or mes=="Noviembre" or mes=="noviembre" or mes=="Diciembre" or mes=="diciembre":
    print(f'La estación del mes {mes} es Otoño')
else: 
    print("El mes fue ingresado erróneamente")


