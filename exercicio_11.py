#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo
#que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a
#balança já desconte o peso do prato.

print("Digite o preco do quilo da camida: ")
comida = float(input())

print("Digite o peso do prato montado: ")
peso = float(input())


valor = comida * peso

print(valor)
