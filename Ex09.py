from random import randint
dado = []
contador_um = 0
contador_dois = 0
contador_tres = 0
contador_quatro = 0
contador_cinco = 0
contador_seis= 0
for valor in range(0, 100):
    valores_dado = randint(1, 6)
    dado.append(valores_dado)
    if 1 == valores_dado:
        contador_um += 1
    elif 2 == valores_dado:
        contador_dois +=1
    elif 3 == valores_dado:
        contador_tres += 1
    elif 4 == valores_dado:
        contador_quatro += 1
    elif 5 == valores_dado: 
        contador_cinco += 1
    else:
        contador_seis += 1
print(dado)
print(f'O número 1 apareceu {contador_um} vezes.')
print(f'O número 2 apareceu {contador_dois} vezes.')
print(f'O número 3 apareceu {contador_tres} vezes.')
print(f'O número 4 apareceu {contador_quatro} vezes.')
print(f'O número 5 apareceu {contador_cinco} vezes.')
print(f'O número 6 apareceu {contador_seis} vezes.')