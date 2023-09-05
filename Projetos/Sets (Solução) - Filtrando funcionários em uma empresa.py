funcionarios =['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melisa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


# Lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

# Lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#Lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
