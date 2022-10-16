# Faça um programa que leia um vetor de 10 posições e verifique se
# existem valores iguais e os escreva na tela.'



from array import array


num = 0
array = []
repetidos = []
for i in range(0,10):
    num = int(input("Digite um valor pro vetor:"))
    array.append(num)

# 
# verificar se existem valores iguais

for i in array:
    array.count(i)
    if array.count(i) > 1:
        repetidos.append(i)
#printar caso tenha ou nao
if repetidos == []:
    print("Nao existem valores repetidos")
else:
    print(f"Os valores repetidos sao {set(repetidos)}")
    
    