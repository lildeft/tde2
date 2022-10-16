# Faça um programa que leia um vetor de 15 posições e o compacte, ou
# seja, elimine as posições com valor zero. Para isso, todos os elementos
# a frente do valor zero, devem ser movidos uma posição para trás no
# vetor.

num = 0
array = []
for i in range(0,15):
     num = int(input("Digite um valor pro vetor:"))
     array.append(num)

for i in array:
    array.remove(0)

print(array)