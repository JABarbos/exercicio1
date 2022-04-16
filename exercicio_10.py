#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o
#preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no
#tanque.

print("Digite o preco da gasolina: ")
gasolina = float(input())

print("Digite o valor do pagamento: ")
pagamento = float(input())


litros = gasolina / pagamento

print(litros)
