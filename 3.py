# Faça um programa que preenche um vetor com valores inteiros até que
# o usuário digite um valor negativo (o valor negativo não deve ser
# inserido no vetor). Imprima:
# a. O vetor.
# b. A quantidade de valores maiores que 5.
# c. A soma dos valores pares armazenados no vetor.
# d. A soma dos valores ímpares armazenados no vetor.
# e. A quantidade total de valores armazenados no vetor
num = 0

array = []



while True:
    
    num = int(input("Digite valores para o vetor (um numero negativo encerra o input)"))
    if num > 0:array.append(num)
    else:
        break

maiorCinco = [numero for numero in array if numero > 5]

pares = [numero for numero in array if numero % 2 == 0]

impares = [numero for numero in array if numero % 2 != 0]

print(f"Vetor = {array}")
print("-"*40)
print(f"A quantidade de valores maior que 5 eh {len(maiorCinco)}")
print("-"*40)
print(f"A soma dos valores pares eh {sum(pares)}")
print("-"*40)
print(f"A soma dos valores impares eh {sum(impares)}")
print("-"*40)
print(f"A quantidade de valores dentro do vetor eh {len(array)}")

