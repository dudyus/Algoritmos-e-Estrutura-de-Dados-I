# 4. Uma palavra é dita palíndrome quando pode ser lida nos 2 sentidos. Elabore um programa que leia
# uma palavra e informe se ela é ou não palíndrome.
# Palavra: mussum
# mussum é Palíndrome

palavra = input("Palavra: ")

if palavra == palavra[::-1]:
    print(f"Palavra: {palavra}")
    print(f"{palavra} é Palíndrome")
else: 
    print(f"Palavra: {palavra}")
    print(f"{palavra} não é Palíndrome")

