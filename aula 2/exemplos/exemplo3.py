# Repetições com for

# range(10): vai de 0 a 9
for i in range(10):
    print(i)

# pode-se acrescentar +1 para obter 1 a 10
for i in range(10):
    print(i+1)

print("-"*30)
# range(1,5): vai de 1 a 4
for i in range(1, 5):
    print(i, end=", ")

print("-"*30)
# range(2, 10, 2): vai de 2 até 8
# valor inicial, valor final(-1), incremento
for i in range(2, 10,2):
    print(i)

print("-"*30)
# Usando for ... range, exibir 10, 9, 8... 1
for i in range(10, 0, -1):
    print(i, end=", ")

# For pode ser aplicado em string usando in
cidade = "Pelotas"
for letra in cidade:
    print(letra)