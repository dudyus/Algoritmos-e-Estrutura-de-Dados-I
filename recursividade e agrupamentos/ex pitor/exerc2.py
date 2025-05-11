def inverter(palavra):
    if len(palavra) == 1:
        return palavra
    else:
        #return palavra[::-1]
        return palavra[-1] + inverter(palavra[0:-1])

palavra = input("Digite: ")
c = inverter(palavra)
print(c)
