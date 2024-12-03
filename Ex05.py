#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
#  O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um 
# vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um 
# total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
#  salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
lista = []
porcento_oito = 8
quantidade = int(input("Quantidade de vendedores na empresa:"))
for vendedor in range(quantidade):
    print(f'VENDEDOR {vendedor}')
    venda = float(input("Valor total das vendas da semana: "))
    print('=-'*15)
    salario = ((porcento_oito/100)*venda)+ 200
    lista.append(salario)
vendedores_no_intervalo01 = list(filter(lambda x: 200 <= x <= 299, lista))
vendedores_no_intervalo02 = list(filter(lambda x: 300 <= x <= 399, lista))
vendedores_no_intervalo03 = list(filter(lambda x: 400 <= x <= 499, lista))
vendedores_no_intervalo04 = list(filter(lambda x: 500 <= x <= 599, lista))
vendedores_no_intervalo05 = list(filter(lambda x: 600 <= x <= 699, lista))
vendedores_no_intervalo06 = list(filter(lambda x: 700 <= x <= 799, lista))
vendedores_no_intervalo07 = list(filter(lambda x: 800 <= x <= 899, lista))
vendedores_no_intervalo08 = list(filter(lambda x: 900 <= x <= 999, lista))
vendedores_no_intervalo09 = list(filter(lambda x: x >= 1000, lista))

print(f'Quantidade de vendedores na faixa salarial de $200 - $299: {len(vendedores_no_intervalo01)}')
print(f'Quantidade de vendedores na faixa salarial de $300 - $399: {len(vendedores_no_intervalo02)}')
print(f'Quantidade de vendedores na faixa salarial de $400 - $499: {len(vendedores_no_intervalo03)}')
print(f'Quantidade de vendedores na faixa salarial de $500 - $599: {len(vendedores_no_intervalo04)}')
print(f'Quantidade de vendedores na faixa salarial de $600 - $699: {len(vendedores_no_intervalo05)}')
print(f'Quantidade de vendedores na faixa salarial de $700 - $799: {len(vendedores_no_intervalo06)}')
print(f'Quantidade de vendedores na faixa salarial de $800 - $899: {len(vendedores_no_intervalo07)}')
print(f'Quantidade de vendedores na faixa salarial de $900 - $999: {len(vendedores_no_intervalo08)}')
print(f'Quantidade de vendedores na faixa salarial de $1000 - ou mais: {len(vendedores_no_intervalo09)}')
