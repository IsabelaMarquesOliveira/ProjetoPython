# Crie um loop que peça ao usuário para digitar o nome de uma fruta.
# Se a fruta digitada não for 'Maça', o loop deve continuar pedindo para digitar o nome de uma fruta.

while True:
    fruta = input('Digite o nome de uma fruta: ')
    if fruta.lower() == 'Maça':
        break 
print('Parbéns, você acertou a fruta!')