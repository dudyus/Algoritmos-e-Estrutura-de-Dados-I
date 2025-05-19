numeros = [5, 12, 20, 25, 31]
print(numeros)

dobros = [num*2 for num in numeros]
print(dobros)

pares = [num for num in numeros if num % 2 == 0]
print(pares)

# pares = []
# for num in numeros:
#     if num % 2 == 0:
#         pares.append(num) 

impares_convertidos = [num+1 for num in numeros if num % 2 == 1]
print(impares_convertidos)