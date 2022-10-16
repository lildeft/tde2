# Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
# eliminando elementos repetidos.


num = 0
array = []
for i in range(0,20):
    num = int(input("Digite um valor pro vetor:"))
    array.append(num)

print(f"Os elementos do vetor sem repeticoes sao {set(array)}")