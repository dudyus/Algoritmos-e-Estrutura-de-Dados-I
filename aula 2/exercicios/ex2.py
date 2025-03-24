# 2. Um número é dito perfeito, quando é igual a soma dos seus divisores (exceto com o próprio
# número). Ler um número, exibir os seus divisores e informar se ele é ou não perfeito.
# Número: 28
# Divisores do 28: 1, 2, 4, 7, 14
# Soma dos divisores: 28
# Portanto, 28 é um número perfeito

numero = int(input("Número: "))
divisores = [i for i in range(1, numero) if numero % i == 0]
somaDivisores = sum(divisores)

if numero == somaDivisores:
    print(f"Número: {numero}")
    print(f"Divisores de {numero}: {divisores}")
    print(f"Soma dos divisores: {somaDivisores}")
    print(f"Portanto, {numero} é um número perfeito.")
else:
    print(f"Número: {numero}")
    print(f"Divisores de {numero}: {divisores}")
    print(f"Soma dos divisores: {somaDivisores}")
    print(f"Portanto, {numero} não é um número perfeito.")
   