def inverte_palavra(palavra):  # recebe o parametro palavra 
    if len(palavra) == 1:
        print(palavra)
    else:
        print(palavra[-1], end="")  # -1 => a ultima letra de palavra
        inverte_palavra(palavra[0:-1])  # começa em 0 (1ª letra) e -1 termina antes da ultima letra

palavra = input("Digite uma palavra: ")  # input tem que ser fora da função 
inverte_palavra(palavra)