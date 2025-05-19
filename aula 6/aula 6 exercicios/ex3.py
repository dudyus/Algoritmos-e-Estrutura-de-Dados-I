# 3. Dada uma lista de números, crie uma segunda lista apenas com raiz quadrada dos números da lista original
# que possuem raiz quadrada exata
# o numeros = [10, 16, 20, 25, 36, 40]
# o numeros2 = [4, 5, 6]
import math

numeros = [10, 16, 20, 25, 36, 40]
print(numeros)

numeros2 = [int(math.sqrt(num)) for num in numeros if math.sqrt(num) * math.sqrt(num) == num]
print(numeros2)
