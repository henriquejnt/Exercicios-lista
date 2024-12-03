#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
lista_maior = []
contador = 0
for v in range(3):
    n1 = float(input("valor :"))
    if n1 in lista:
        contador += 1
        lista.remove(n1)
    lista.append(n1)
if contador >= 1 :
    for maior in range(3-contador):
        maior = max(lista)
        lista_maior.append(maior)
        lista.remove(maior)
else:
    for maior in range(3):
        maior = max(lista)
        lista_maior.append(maior)
        lista.remove(maior)
print(lista_maior)