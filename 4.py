# Crie um programa que lê 6 valores inteiros, armazene-os em um vetor e,
# em seguida, mostre na tela os valores lidos na ordem inversa.
num = 0
array = []
for i in range(0,6):
    num = int(input("Digite um valor para o vetor:"))
    array.append(num)
    
#vec.sort(reverse = True)
# Usar o sort tava dando uma ordem decrescente e nao uma ordem inversa entao achei isso aqui
# que eh basciamente um fatiamento do vetor com um passo inverso 
# > (valor[::-1]) < 

print(array[::-1])