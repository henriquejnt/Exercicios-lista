lista = []
maior_media = 0
menor_sete = 0
contador = 0
while True:
    valor = int(input('Digite um valor [negativo para parar]: '))
    if valor < 0:
        break
    #se o valor tiver na lista novamente
    if valor in lista:
        lista.remove(valor)
    else:
        lista.append(valor)
        contador += 1
#calculos
media = (sum(lista))/len(lista)
for medida in lista:
    if medida > media:
        maior_media += 1
    
    if medida < 7:
        menor_sete +=1
print('=-'*15)
print(f'Quantidade de valores que foram lidos: {len(lista)}')
print(f'Todos os valores na ordem em que foram informados: {lista}')
print(f'Valores na ordem inversa: {lista[::-1]}')
print(f'Soma dos valores: {sum(lista)}')
print(f'Média dos valores: {media}')
print(f'Quantidade de valores acima da média: {maior_media}')
print(f'Quantidade de valores menor que sete: {menor_sete}')
print('Programa finalizado  com sucesso!')