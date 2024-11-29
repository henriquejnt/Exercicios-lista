#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = []
for valor in range(5):
    num = float(input('Digite o valor: '))
    lista.append(num)
print(lista)