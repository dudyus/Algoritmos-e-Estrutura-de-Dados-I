# 5. Elaborar um programa que leia ‘n’ números, até ser digitado 0. Ao final, exiba quantos números
# foram digitados, a soma dos números e qual o maior número digitado.
# Informe números ou 0 para sair
# Número: 12
# Número: 39
# Número: 13
# Número: 26
# Número: 0
# -----------------------------
# Números digitados: 4
# Soma dos Números: 90
# Maior Número: 39

numero = int(input("Número: "))

while True:
   
    numero = int(input("Número: "))
    if numero <= 0:
        print("vc saiu")
        break