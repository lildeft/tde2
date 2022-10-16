# Faça um programa que preenche um vetor de 50 posições com valores (0,51)
# aleatórios entre 0 e 20 e encontre:
# Obs: Para fazer um vetor de tamanho 50 preenchido com 0 é possível fazer:
# vetor = [0] * 50. Note que o valor 50 também pode ser substituído por uma variável
# qualquer.
# a. A soma dos valores armazenados no vetor.
# b. O número de ocorrências do valor 9.
# c. O maior valor armazenado no vetor.
# d. O menor valor armazenado no vetor.

from random import randint


array = []


#geracao do vetor aleatorio utilizando biblioteca
for i in range(0,50):
    i = randint(0,20)
    array.append(i)


print(f"Vetor = {array}")
print("-"*40)
print(f"A soma dos valores do vetor eh {sum(array)}")
print("-"*40)
print(f"O numero 9 se repete {array.count(9)} vezes")
print("-"*40)
print(f"O maior valor armazenado no vetor eh {max(array)}")
print("-"*40)
print(f"O menor valor armazenado no vetor eh {min(array)}")

