# Repetições com while

continua = "S"
while continua == "S":
    print("Olá...")
    continua = input("Continuar: ").upper()

print("-"*30)
# Outra forma mais usual

while True:
    print("Oi...")
    continua = input("Continuar: ").upper()

    if continua == "N":
        print("Você escolheu sair...")
        break