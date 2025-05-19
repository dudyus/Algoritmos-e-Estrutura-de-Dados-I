# Aplicação  com dicionáros: Lista de dicionários

clientes = [
    {"nome": "Pedro Santos", "idade": 30},
    {"nome": "Aline Costa", "idade": 42},
    {"nome": "Maria de Mattos", "idade": 25},
    {"nome": "Carlos de Nóbrega", "idade": 34},
    {"nome": "Bianca Cardoso", "idade": 27},
]

# Pode-se acrescentar itens na lista
clientes.append({"nome": "Lucas de Souza", "idade": 20})

# Exibir elementos da lista
print(clientes[0])

# Apenas um atributo de um elemento
print(clientes[0]["nome"])

# Formas de percorrer a lista de dicionarios
for cliente in clientes:
    print(cliente["nome"])

# Uso do enumarate
for num, cliente in enumerate(clientes, start=1):
    print(f"{num}° cliente: {cliente["nome"]}")

# ------- Formas de classificar/ordenar a lista
# lambda: forma de declarar funcções anonima no python
# Equivale as arrow functions () => {} do JavaScript 
clientes2 = sorted(clientes, key=lambda cliente: cliente["nome"])

print("*"*30)
for num, cliente in enumerate(clientes2, start=1):
    print(f"{num}° cliente: {cliente["nome"]}")

# ---------- Em ordem decrescente
clientes3 = sorted(clientes, key=lambda cliente: cliente["idade"],
                   reverse=True)

print("*"*30)
for num, cliente in enumerate(clientes3, start=1):
    print(f"{num}° cliente: {cliente["nome"]} - {cliente["idade"]} anos")

# ------ Filtros na lista
print("#"*30)
for num, cliente in enumerate(clientes3, start=1):
    if (cliente["idade"]>=30):
        print(f"{num}° cliente: {cliente["nome"]} - {cliente["idade"]} anos")

# -------- Filtros c list comprehensions
clientes4 = [x for x in clientes if x["idade"] < 30]

print("*"*30)
for num, cliente in enumerate(clientes4, start=1):
        print(f"{num}° cliente: {cliente["nome"]} - {cliente["idade"]} anos")

print()
num = len(clientes4)
print(f"{num} clientes menore que 30 anos")