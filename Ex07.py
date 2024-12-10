votos = {}
camisas = []
while True:
    try:
        n = int(input('Número do Jogador [0=parar]: '))
    except ValueError:
        n = int(input('TENTE NOVAMENTE:Número do Jogador [0=parar]: '))
    else:
        if n < 0 or n == 0:
            break
        else:
            camisas.append(n)
            if n in votos :
                votos[n] += 1
            else:
                votos[n] = 1
print('JOGADOR')
for num in camisas:
    print(f"Camisa {num}")
print(votos)
for valor, vt in votos.items():
    print(f'Camisa {valor}: votos {vt}')