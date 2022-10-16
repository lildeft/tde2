# Crie um programa com dois vetores de 10 posições e insira em outro
# vetor, nas posições pares, os valores do primeiro e, nas posições
# ímpares, os valores do segundo.



from typing import final


array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [11,12,13,14,15,16,17,17,19,20]

finalArray = [0] * 10

for i in range(len(finalArray)):
    if i % 2 == 0:
        finalArray[i] = array1[i]
    if i % 2 != 0:
        finalArray[i] = array2[i]

print(finalArray)
