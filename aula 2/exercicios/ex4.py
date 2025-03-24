# 4. Digamos que o número de chinchilas de uma fazenda triplica a cada ano, após o primeiro ano.
# Elaborar um programa que leia o número inicial de chinchilas e anos e informe ano a ano o número
# médio previsto de chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou igual a 2
# (um casal).
# Número de Chinchilas: 8
# Anos da criação: 6
# 1º Ano: 8 chinchilas
# 2º Ano: 24 chinchilas
# 3º Ano: 72 chinchilas
# 4º Ano: 216 chinchilas
# 5º Ano: 648 chinchilas
# 6º Ano: 1944 chinchilas

chinchilas = int(input("Número de Chinchilas: "))
anosCria = int(input("Anos de criação: "))

if chinchilas >= 2:
    for i in range(1, anosCria + 1):
        totalChinchilas = chinchilas * (3 ** (i - 1)) # ** = potencia -> 1°ano 3 elevado a (1-1) = 3 elevado a 0
        print(f"{i}° ano: {totalChinchilas} chinchilas")
else:
    print("O número de chinchilas deve ser no mínimo 2")


