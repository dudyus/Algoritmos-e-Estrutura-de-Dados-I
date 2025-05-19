import csv

titanic = []

# Lê os dados do arquivo e joga em uma lista de dicionarios (titanic)
with open("train.csv", mode="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        titanic.append(linha)

# print(titanic[0])
# print(titanic[0]["Name"])

def titulo(mensa, traco="-"):
    print()
    print(mensa.upper())
    print(traco*50)

def dados_sexo():
    titulo("Dados por sexo")
    print("Total de passageiros")

    # pegar o n° de PASSAGEIROS homens
    masculino = [x for x in titanic if x["Sex"] == "male"]
    num_masc = len(masculino)
    print(f"Masculino: {num_masc} ")

    # pegar o N° de SOBREVIVENTES masculinos
    masc_sobre = [x for x in titanic if x["Sex"] == "male" and int(x["Survived"]) == 1]
    num_sobre = len(masc_sobre)
    print(f"    Sobreviventes: {num_sobre}")

    # pegar o n° de homens que morreram
    masc_mortos = [x for x in titanic if x["Sex"] == "male" and int(x["Survived"]) == 0]
    num_mortos = len(masc_mortos)
    print(f"    Mortos: {num_mortos}")

    # pegar o n° de PASSAGEIRAS
    feminino = [x for x in titanic if x["Sex"] == "female"]
    num_fem = len(feminino)
    print(f"Feminino: {num_fem}")

     # pegar o N° de SOBREVIVENTES femininas
    fem_sobre = [x for x in titanic if x["Sex"] == "female" and int(x["Survived"]) == 1]
    num_sobre = len(fem_sobre)
    print(f"    Sobreviventes: {num_sobre}")

    # pegar o n° de mulheres que morreram
    fem_mortas = [x for x in titanic if x["Sex"] == "female" and int(x["Survived"]) == 0]
    num_mortas = len(fem_mortas)
    print(f"    Mortos: {num_mortas}")

    # Total de Passageiros
    # Masculino: x
    #   Sobreviventes: x
    #   Mortos: x
    # Feminino: x
    #   Sobreviventes: x
    #   Mortos: x

def media_top10():
    titulo("Média e Top10 +Idosos")

    # pegar as idades e suas medias
    idade = [float(x["Age"]) for x in titanic if x["Age"] != ""]
    # idade = [x for x in titanic if x["Age"] != ""]
    num_idade = len(idade) 
    soma_idades = sum(idade)
    media = soma_idades / num_idade
    print(f"Média das Idades: {media:.1f}")
    print("Lista dos mais idosos")
    print("N°  Nome...................   Idade:  Sobrevivente: ")
    # Listar os mais idosos
    passageiros = [x for x in titanic if x["Age"] != ""]
    idosos = sorted(passageiros, key=lambda titanic: float(titanic["Age"]), reverse=True) 
    for num, passageiro in enumerate(idosos[:10], start=1):
        if int(passageiro["Survived"]) == 1:
            sobrevivente = "Sim"
        else: 
            sobrevivente = "Não"
        print(f"{num}°. {passageiro["Name"]} - {passageiro["Age"]} anos - {sobrevivente}")

    # Média das Idades: x
    # Lista dos +Idosos
    # N° Nome.................: Idade: sobrevivente
    # XX XXXXXXXXXXXXXXXXXXXXXX  XX     Sim/Não

def dados_classe():
    titulo("Dados por classe")
    print("Total de passageiros")

    # pegar passageiros da 1ª classe
    first_class = [x for x in titanic if int(x["Pclass"]) == 1]
    num_first = len(first_class)

    # pegar sobreviventes da 1ª classe
    first_sobre = [x for x in titanic if int(x["Pclass"]) == 1 and int(x["Survived"]) == 1]
    num_sobre = len(first_sobre)

    # pegar os mortos da 1ª classe
    first_mortos = [x for x in titanic if int(x["Pclass"]) == 1 and int(x["Survived"]) == 0]
    num_mortos = len(first_mortos)

    porcentagem_sobre = (num_sobre / num_first) * 100   
    porcentagem_mortos = (num_mortos / num_first) * 100
 
    # mostrar 1ª classe
    print(f"1ª Classe: {num_first}")
    print(f"    Sobreviventes: {num_sobre} - {porcentagem_sobre:.2f}%")
    print(f"    Mortos: {num_mortos} - {porcentagem_mortos:.2f}%")

    # pegar passageiros da 2ª classe
    sec_class = [x for x in titanic if int(x["Pclass"]) == 2]
    num_sec = len(sec_class)
    
    # pegar sobreviventes da 2ª classe
    sec_sobre = [x for x in titanic if int(x["Pclass"]) == 2 and int(x["Survived"]) == 1]
    num_sobre = len(sec_sobre)
    
    # pegar os mortos da 2ª classe
    sec_mortos = [x for x in titanic if int(x["Pclass"]) == 2 and int(x["Survived"]) == 0]
    num_mortos = len(sec_mortos)
   
    porcentagem_sobre = (num_sobre / num_sec) * 100   
    porcentagem_mortos = (num_mortos / num_sec) * 100

    # mostrar 2ª classe
    print(f"2ª Classe: {num_sec}")
    print(f"    Sobreviventes: {num_sobre} - {porcentagem_sobre:.2f}%")
    print(f"    Mortos: {num_mortos} - {porcentagem_mortos:.2f}%")

    # pegar passageiros da 3ª classe
    third_class = [x for x in titanic if int(x["Pclass"]) == 3]
    num_third = len(third_class)
    
    # pegar sobreviventes da 3ª classe
    third_sobre = [x for x in titanic if int(x["Pclass"]) == 3 and int(x["Survived"]) == 1]
    num_sobre = len(third_sobre)
   
    # pegar os mortos da 3ª classe
    third_mortos = [x for x in titanic if int(x["Pclass"]) == 3 and int(x["Survived"]) == 0]
    num_mortos = len(third_mortos)
   
    porcentagem_sobre = (num_sobre / num_third) * 100   
    porcentagem_mortos = (num_mortos / num_third) * 100

    print(f"3ª Classe: {num_third}")
    print(f"    Sobreviventes: {num_sobre} - {porcentagem_sobre:.2f}%")
    print(f"    Mortos: {num_mortos} - {porcentagem_mortos:.2f}%")

    #Total de Passageiros
    # 1ª Classe: x
    #   Sobreviventes:x - x%
    #   Mortos:x - x%
    # 2ª Classe: x
    #   Sobreviventes:x - x%
    #   Mortos:x - x%
    # 3ª Classe: x
    #   Sobreviventes:x - x%
    #   Mortos:x - x%

while True:
    titulo("Passageiros do Titanic", "=")
    print("1. Dados por Sexo e Sobreviventes")
    print("2. Média de Idade e 10+ Idosos")
    print("3. Dados por Classe e Sobreviventes")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        dados_sexo()
    elif opcao == 2:
        media_top10()
    elif opcao == 3:
        dados_classe()
    else:
        break