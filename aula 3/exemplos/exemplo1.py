palavra = "computador"

letra = input("Letra: ").upper()

if palavra.upper().find(letra) >= 0:
    print("Ok! Letra consta na palavra.")
else:
    print("Erro... Letra não consta")