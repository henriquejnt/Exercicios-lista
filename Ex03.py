#Faça um Programa que leia um vetor A com 10 números inteiros, calcule 
# e mostre a soma dos quadrados dos elementos do vetor.
lista = []
lista_quadrado = []
for valor in range(10):
    n1 = float(input('Valor: '))
    lista.append(n1)
for quadrado in lista:
    lista_quadrado.append(quadrado**2)
print(f'A soma dos quadrados dos elementos é {sum(lista_quadrado)}')