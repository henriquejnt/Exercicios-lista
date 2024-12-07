while True:
    lista_saltos = []
    nome = input('Nome do atleta: ')
    if nome == '':
        break
    else:
        for atleta in range(1, 6):
            saltos = float(input(f'{atleta} salto: '))
            lista_saltos.append(saltos)
            if atleta == 5:
                print('=-'*15)
                print(f'Nome atleta: {nome}')
                print(f'Saltos: {lista_saltos}')
                print(f'Média dos saltos: {sum(lista_saltos)/(len(lista_saltos)):.2f}m')
                print('=-'*15)
