# 3. Elaborar um programa que leia o nome de um produto e o número de etiquetas a serem
# impressas desse produto. Exiba as etiquetas com o nome do produto, com no máximo 2 etiquetas
# por linha, conforme exemplo de execução do programa, demonstrado a seguir.
# Produto: Suco Natural de Uva
# Nº de Etiquetas: 7
# Suco Natural de Uva Suco Natural de Uva
# Suco Natural de Uva Suco Natural de Uva
# Suco Natural de Uva Suco Natural de Uva
# Suco Natural de Uva

produto = input("Produto: ")
numEtiquetas = int(input("N° de etiquetas: "))

for i in range(0, numEtiquetas, 2):
    print(produto, end=" ")
    if i+1 < numEtiquetas:  # verifica se tem espaço pra mais uma etiqueta na linha
        print(produto)
    else:
        print()