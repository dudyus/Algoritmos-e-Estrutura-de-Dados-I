import csv

fakeNews = []

with open("fake_news_dataset.csv", mode="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        fakeNews.append(linha)

def top10_fontes():
    print("")
    print("Jornais com mais Artigos falsos")
    print("-"*40)
    
    fontes_fake = {}

    for artigo in fakeNews:
        fonte = artigo['source']
        status = artigo['label']

        if status == "fake" and fonte:
            fontes_fake[fonte] = fontes_fake.get(fonte, 0) + 1
        
    fontes_fake2 = dict(sorted(fontes_fake.items(), key=lambda item: item[1], reverse=True))

    print("N° Nome da Fonte......: Artigos Falsos...:")

    for num, (fonte, status) in enumerate(fontes_fake2.items(), start=1):
        print(f"{num:2} {fonte:20s} {status:18}")
        if num == 10:
            break

def top10_categorias():
    print("")
    print("Categorias mais Abordadas em Artigos Falsos")
    print("-"*40)
    
    categorias_abordadas = {}
    
    for artigo in fakeNews:
       categoria = artigo['category']
       
       if categoria:
           categorias_abordadas[categoria] = categorias_abordadas.get(categoria, 0) + 1

    categorias_abordadas2 = dict(sorted(categorias_abordadas.items(), key=lambda item: item[1], reverse=True))

    print("N° Categoria.......:")

    for num, (categoria, num_abordagens) in enumerate(categorias_abordadas2.items(),start=1):
        print(f"{num:2} {categoria}")
        if num == 10:
            break

def comparar_fontes():
    print("")
    print("Comparar 2 Fontes")
    print("-"*40)
    fonte1 = input("1° Fonte: ")
    fonte2 = input("2° Fonte: ")
    
    porcentagem1 = calcula_porcentagem(fonte1.upper())
    porcentagem2 = calcula_porcentagem(fonte2.upper())

    if porcentagem1 is None:
        print(f"Fonte '{fonte1}' Não tem artigos")
    else:
        print(f"Fonte 1: {fonte1} - {porcentagem1:.2f}% de artigos falsos")
    
    if porcentagem2 is None:
        print(f"Fonte '{fonte2}' Não tem artigos")
    else: 
        print(f"Fonte 2: {fonte2} - {porcentagem2:.2f}% de artigos falsos")

def pesquisar_autor_categoria():
    while True:
        print("")
        print("Pesquisar Autor ou Categoria")
        print("-"*40)
        print("1. Autor")
        print("2. Categoria")
        print("3. Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            print("")
            print("Pesquisa Autor")
            print("-"*40)
            nomeAutor = input("Nome do Autor: ")

            autores = set([artigo['author'] for artigo in fakeNews if nomeAutor.upper() in artigo['author'].upper()])

            autores2 = sorted(list(autores))

            if len(autores2) == 0:
                print(f"\n* Não há autores com o nome: {nomeAutor}")
            else:
                print(f"\nNome do autor......: ")
                print(   "----------------------------------------------")

                for autor in autores:
                    print(f"{autor:20s}")

        elif opcao == 2:
            print("")
            print("Pesquisa Categoria")
            print("-"*40)
            nomeCategoria = input("Nome da Categoria: ")

            categorias = set([artigo['category'] for artigo in fakeNews if nomeCategoria.upper() in artigo['category'].upper()])

            categorias2 = sorted(list(categorias))

            if len(categorias2) == 0:
                print(f"\n* Não há categorias com o nome: {nomeCategoria}")
            else:
                print(f"\nCategoria......: ")
                print(   "----------------------------------------------")

                for categoria in categorias2:
                    print(f"{categoria:20s}")
        else: 
            break


# def palavras_chave():
#     print("")
#     print("Análise de Autores por Palavras-Chave")
#     print("-" * 40)

#     palavra1 = input("Digite a 1ª palavra-chave: ").strip().upper()
#     palavra2 = input("Digite a 2ª palavra-chave: ").strip().upper()
    

# def autores_ambas_palavras():
#     print("\nAnálise de Autores por Duas Palavras-Chave")
#     print("-" * 40)

#     palavra1 = input("Digite a 1ª palavra-chave: ").strip().upper()
#     palavra2 = input("Digite a 2ª palavra-chave: ").strip().upper()

#     autores1 = set()
#     autores2 = set()

#     for artigo in fakeNews:
#         titulo = artigo.get('title', '').upper()
#         autor = artigo.get('author', 'Desconhecido')

#         if palavra1 in titulo:
#             autores1.add(autor)
#         if palavra2 in titulo:
#             autores2.add(autor)

#     autores_em_ambas = sorted(list(autores1.intersection(autores2)))

#     if autores_em_ambas:
#         print(f"\nAutores que escreveram sobre **ambas** as palavras '{palavra1}' e '{palavra2}':")
#         for autor in autores_em_ambas:
#             print(f" - {autor}")
#     else:
#         print(f"\nNenhum autor escreveu sobre **ambas** as palavras '{palavra1}' e '{palavra2}'.")


def calcula_porcentagem(fonte):
    total_artigos = 0
    artigos_falsos = 0

    for artigo in fakeNews:
        if artigo['source'].upper() == fonte:
            total_artigos += 1
            if artigo['label'] == "fake":
                artigos_falsos += 1
    if total_artigos == 0: 
        return None
    
    porcentagem = (artigos_falsos / total_artigos) * 100
    return porcentagem
    
while True:
    print("")
    print("Estatísticas: Detecção de Fake News")
    print("-"*40)
    print("1. Top 8 Fontes com mais Artigos falsos")
    print("2. Top 7 Categorias mais Abordadas")
    print("3. Comparar 2 Fontes")
    print("4. Pesquisar por Autor ou Categoria")
    print("5. Analisar Autor por Palavras-Chaves")
    print("6. Finalizar")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        top10_fontes()
    elif opcao == 2:
        top10_categorias()
    elif opcao == 3:
        comparar_fontes()
    elif opcao == 4:
        pesquisar_autor_categoria()
    elif opcao == 5:
        autores_ambas_palavras()
    else:
        break


# 1) Top 10 fontes com mais artigos falsos
# - Agrupar dados e depois mostrar (source / label)
# * BBC - 500 artigos fake
# 2) Top 10 categorias mais abordadas
# - Pegar atributo e ordenar ele sem agrupar nem nada
# * Politica
# * Saúde
# * Trabalho
# 3) Comparar 2 fontes
# - Pega 2 fontes e compara a média de artigos fake
# *BBC - 72% fake
# *The town - 38% fake
# 4) Pesquisar por autor ou categoria
# - Coloca o nome do autor
# - Coloca a categoria 
# 5) Analisar autor por palavra chave
# - Insere a palavra chave "Covid", retorna;
# * Todos autores que ja postaram sobre "Covid"
# * Todos autores que nunca postaram sobre "Covid"