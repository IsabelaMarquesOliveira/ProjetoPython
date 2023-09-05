# Calculo de IMC - Indice de Massa Corporal 
# Menor que 18,5  - Magreza
# Entre 18,5 e 24,9  - Normal
# Entre 25,0 e 29,9 - Sobrepeso
# Entre 30,0 e 39,9 - Obesidade
# Maior que 40,0 - Obesidade Grave
 
altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('Magreza')
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')


