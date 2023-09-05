rendimento = int(input('Qual é o rendimento da lata?'))
altura = int(input('Qual é a altura da parede?'))
largura = int(input ('Qual é a largura da parede?'))

#funções

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()