# 2. Elaborar um programa que leia o nome completo de um aluno. Valide o nome para que seja composto.
# Exiba apenas o primeiro nome do aluno em letras maiúsculas.
# Nome Completo: Maria
# Ops... Por favor, digite o nome completo
# Nome Completo: Maria dos Santos
# Nome no Crachá: MARIA

nome = input("Nome Completo: ")
composto = False
cracha = nome.split(" ")


for letra in nome:
    if letra.isspace():
        composto = True

if composto == True:
    print("-"*30)
    print(f"Nome Completo: {nome}")
    print(f"Nome no Crachá: {cracha[0].upper()}")
else:
    print("Ops... Por favor, digite o nome completo")
