
contador = 0
km1000_por_carro = []
modelos_carros  = ['Chevrolet Onix',15,'Volkswagen Polo',14,'Fiat Strada',13,'Toyota Corolla ',12,'Jeep Compass',10]
for carro in range (len(modelos_carros)):
    if carro % 2 == 0:
        print('=-'*15)
        contador += 1
        print(f'{contador} carro')
        print(f'Nome do carro: {modelos_carros[carro]}')
    else:
        km1000_por_carro.append(1000 / modelos_carros[carro] )
        print(f'Km por litro: {modelos_carros[carro]}')
contador = 0
contador_km = 0
print('=-'*15)
print('RELATÓRIO FINAL')
for carro in range (len(modelos_carros)):
    contador += 1
    if carro % 2 ==0:
        print(f'{contador} - {modelos_carros[carro]:<15}       - ', end="")
    else:
        print(f'{modelos_carros[carro]:>5.1f}- ', end="")
        print(f'{km1000_por_carro[contador_km]:>5.1f} litros - ', end="")
        print(f'R${km1000_por_carro[contador_km]*2.25:.2f}')
        contador_km += 1
