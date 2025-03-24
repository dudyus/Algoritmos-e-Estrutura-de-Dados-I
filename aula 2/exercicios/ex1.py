# 1. A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um
# peixe. Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma
# família que foram ao clube e o número de peixes obtidos na pescaria. Informe o valor a pagar.
# Nº Pessoas: 4
# Nº Peixes: 5
# Pagar R$: 92.00

numPessoas = int(input("N° de Pessoas: "))
numPeixes = int(input("N° de Peixes: "))

if numPeixes == numPessoas:
    valorFinal = (20 * numPessoas) 
    print(f"Pagar R$: {valorFinal}")
else:
    peixeExtra = numPeixes - numPessoas
    valorFinal = (20 * numPessoas) + (peixeExtra * 12) 
    print(f"Pagar R$: {valorFinal}")