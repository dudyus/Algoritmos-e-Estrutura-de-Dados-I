# 1. Dada uma lista de números, crie uma segunda lista apenas com os números da lista original que são
# divisíveis por 10.
# o numeros = [15, 30, 50, 72, 95]
# o Numeros2 = [30, 50]

numeros = [15, 30, 50, 72, 95]
print(numeros)

divisiveis = [num for num in numeros if num % 10 == 0]
print(divisiveis)