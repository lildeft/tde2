# 1. Faça um programa que possua um vetor que armazene 6 números
# inteiros. O programa deve executar os seguintes passos:
# a. Armazene os seguintes valores ao vetor: 1, 0, 5, -2, -5, 7.
# b. Armazene em uma variável a soma dos valores nas posições 0, 1
#  e 5. Imprima na tela a soma.
# c. Modifique o valor da posição 4 para 100.
# d. Imprima na tela cada valor do vetor, um em cada linha.


array = [1, 0, 5, -2, -5, 7]

soma = (array[0]+array[1]+array[5])

print(f"A soma dos valores eh {soma}")

print("-"*40)

array[4]= 100

for i in range(len(array)):
    print(f"Na posicao [{i}] o valor eh {array[i]}")
    
    