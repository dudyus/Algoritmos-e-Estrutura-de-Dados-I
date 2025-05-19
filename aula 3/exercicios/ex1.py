# 1. Elaborar um programa que leia uma senha e informe se ela é válida ou não. Para ser válida a senha
# deve conter letras maiúsculas, minúsculas e números. Além disso, a senha deve possuir entre 8 e 12
# caracteres.
# Senha: abracadabra
# Senha Inválida

senha = input("Digite uma senha: ")

maiuscula = False
minuscula = False
num = False

for letra in senha:
    if letra.isupper():
        maiuscula = True

for letra in senha:
    if letra.islower():
        minuscula = True

for letra in senha:
    if letra.isdigit():
        num = True

if len(senha) >= 8 and len(senha) <= 12:
    if maiuscula == True and minuscula == True and num == True:
        print("Senha Válida")
    else:
        print("Senha Inválida")
else: 
        print("Senha Inválida, deve possuir entre 8 a 12 caracteres")
    
