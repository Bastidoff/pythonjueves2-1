#condiciones anidad ELIF

sensorNivelAgua=int(input("Digite el nivel de agua actual"))

if(sensorNivelAgua>=0 and sensorNivelAgua<20):
    print(f'¡PELIGRO: el nivel {sensorNivelAgua} es eligroso!')
elif(sensorNivelAgua>=20 and sensorNivelAgua<400):
    print(f'La represea funciona OK. Nivel de agua: {sensorNivelAgua}')
elif(sensorNivelAgua>=400):
    print(f'¡PELIGRO: el nivel {sensorNivelAgua} es eligroso!')
else:
    print("El nivel de agua no es válido")

