# ENTRADA DE DADOS  
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário R$: "))

'''

Comentário de Várias linhas
'''

print(f"Seu nome é {nome}")
print(f'Sua idade é {idade} anos')
print(f"Seu salário é de R${salario:9.2f}") #9 digitos e 2 decimais

# CONDIÇÕES
# No Python, a identação indica os comandos dentro
# de um bloco (condição, repetição, função)
if idade < 18:
    print("Você é da categoria infantil")
elif idade <= 50:
    print("Você é da categoria adulto ")
else: 
    print("Você é da categoria Sênior")

print("-"*20)

# match... case
bairro = input("Bairro:").upper()

match bairro:
    case "CENTRO":
        print("Você mora aqui perto...")
    case"FRAGATA" | "TRÊS VENDAS":
        print("Ainda é perto")
    case "LARANJAL":
        print("Ai é longe")
    case _:
        print("Não sei a distância...")    