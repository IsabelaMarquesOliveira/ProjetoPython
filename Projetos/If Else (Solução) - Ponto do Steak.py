temperatura = int(input('Qual é a temperatura da carne?'))

if temperatura < 48:
    print('Cozinhar por mais algund minutos')

elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem')
else:
    print('Bem passada')
