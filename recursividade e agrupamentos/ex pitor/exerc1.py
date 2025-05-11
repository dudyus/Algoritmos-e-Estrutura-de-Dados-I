def inverte(palavra):
    if len(palavra) == 1:
        print(palavra)
    else:
        print(palavra[-1], end="")
        inverte(palavra[0:-1])

palavra = input("Digite uma palvra:")

inverte(palavra)
