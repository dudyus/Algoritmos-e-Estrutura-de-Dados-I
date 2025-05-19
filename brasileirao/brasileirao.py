import csv
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
brasileirao = []

with open("BRA_players.csv", mode="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        brasileirao.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("-"*40)

def top_clubes():
    titulo("Clubes + Valiosos")
    
    valiosos = {}
    
    for jogador in brasileirao:
        clube = jogador['Team']
        # Alguns jogadores não possuem valor de mercado ( preenchido )
        if jogador['Market Value'] == '':
            valor = 0
        else:
            valor = float(jogador['Market Value'])
        valiosos[clube] = valiosos.get(clube, 0) + valor
        #valiosos{'São Paulo': 1000000, 'Vitoria': 900000}
        
    # Ordenar por chave
    valiosos2 = dict(sorted(valiosos.items(),
                key= lambda valioso: valioso[1], reverse=True))
    
    print("Nº Nome do Clube......: R$ Total......:")
    
    for num, (clube, valor) in enumerate(valiosos2.items(), start=1):
        valor2 = locale.currency(valor, grouping=True, symbol=None)
        print(f"{num:2} {clube:20s} {valor2:>15s}")
        if num == 10:
            break

def top_idades():
    titulo("Top 10 Jogadores + Experientes")
    
    jogadores2 = sorted(brasileirao,
                key=lambda jogador: int(jogador['Age']), reverse=True)
    
    print(f"\nNº Nome do Jogador....: Clube..........: Idade.:")
    print(   "----------------------------------------------")
    
    for num, jogador in enumerate(jogadores2, start=1):
        print(f"{num:2d} {jogador['Player']:20s} {jogador['Team']:16s} {jogador['Age']} anos")
        if num == 10:
            break

    titulo("Top 10 Jogadores + Jovens")
    
    jogadores3 = reversed(jogadores2)
    
    print(f"\nNº Nome do Jogador....: Clube..........: Idade.:")
    print(   "----------------------------------------------")
    
    for num, jogador in enumerate(jogadores3, start=1):
        print(f"{num:2d} {jogador['Player']:20s} {jogador['Team']:16s} {jogador['Age']} anos")
        if num == 10:
            break

def comparar_clubes():
    titulo("Compara Clubes:")
    clube1 = input("1º Clube: ")
    clube2 = input("2º Clube: ")
    
    num1 = 0
    soma1 = 0
    num2 = 0
    soma2 = 0
    
    for jogador in brasileirao:
        if jogador['Team'].upper() == clube1.upper():
            num1 = num1 + 1
            soma1 = soma1 + int(jogador['Age'])
        elif jogador['Team'].upper() == clube2.upper():
            num2 = num2 + 1
            soma2 = soma2 + int(jogador['Age'])
    print(f"Média da Idade dos Jogadores do {clube1}: {soma1/num1:4.1f} anos.")
    print(f"Média da Idade dos Jogadores do {clube2}: {soma2/num2:4.1f} anos.")

def pesquisar_jogador():
    titulo("Pesquisa Jogador")
    
    nome = input("Nome do Jogador: ")
    
    lista = [jogador for jogador in brasileirao
            if nome.upper() in jogador['Player'].upper()]
    
    if len(lista) == 0:
        print(f"\n* Não ha jogadores com o nome: {nome}")
    else:
        print(f"\nNome do Jogador....: Clube..........:")
        print(   "----------------------------------------------")
        
        for jogador in lista:
            print(f"{jogador['Player']:20s} {jogador['Team']}")

def analisar_idade():
    titulo("Analise Clubes por Idade:")
    
    idade = int(input("Idade: "))
    
    # Convertemos pra conjunto com "set", eliminando as repetições, ex: 'São Paulo', 'São Paulo', 'São Paulo'
    clubes = set([jogador['Team'] for jogador in brasileirao if int(jogador['Age']) == idade])
    
    # Converter novamente em lista, permite (por exemplo, ordenar)
    clubes2 = sorted(list(clubes))
    
    print(f"Clubes com Jogadores com {idade} anos: {", ".join(clubes2)}")
    
    todos_clubes = set([jogador['Team'] for jogador in brasileirao])
    # Usa o método difference() para "subtrair" todos os clubes de clubes
    clubes_sem = todos_clubes.difference(clubes)
    
    clubes3 = sorted(list(clubes_sem))
    
    print(f"\nClubes que não possuem Jogadores com {idade} anos: {", ".join(clubes3)}")

while True:
    titulo("Estatísticas: Brasileirão 2024")
    print("1. Top 10 Clubes + Valiosos")
    print("2. Top 10 Idades (Jovens/Experientes)")
    print("3. Comparar 2 clubes")
    print("4. Pesquisar Jogador")
    print("5. Analisar por Idade")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top_clubes()
    elif opcao == 2:
        top_idades()
    elif opcao == 3:
        comparar_clubes()
    elif opcao == 4:
        pesquisar_jogador()
    elif opcao == 5:
        analisar_idade()
    else:
        break
