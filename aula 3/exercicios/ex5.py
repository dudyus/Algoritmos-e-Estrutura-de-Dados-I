# 5. Elabore um programa que leia um e-mail de um aluno. Informe se o e-mail está em um formato válido
# ou não. Para ser válido, o e-mail deve possuir um sinal de “@”, um ou mais pontos após o “@” e não
# deve possuir espaços.
# E-mail: anamaria@senacrs.com.br
# Ok! E-mail em formato válido.

email = input("E-mail: ")

tem_arroba = False
tem_espaco = False
tem_ponto = False

if "@" in email:
    tem_arroba = True
    partes = email.split("@")
    if len(partes) == 2 and "." in partes[1]:
        tem_ponto = True


for letra in email:
    if letra.isspace():
        tem_espaco = True


if tem_arroba and tem_ponto and not tem_espaco:
    print(f"E-mail: {email}")
    print("Ok! E-mail em formato válido.")
else: 
    print("O formato de E-mail não é válido.")
