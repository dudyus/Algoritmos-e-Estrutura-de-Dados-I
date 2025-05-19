import random
import time
import os            # pacote com funções do sistema operacional
from colorama import Fore, Back, Style

temp = "🐯🐯🐮🐮🐢🐢🪿🪿🦜🦜🪼🪼🐠🐠🐔🐔"
figuras = list(temp)

nome_jogador = input("Informe seu nome: ")
total_pontos = 0

jogo = []
apostas = []

def preenche_matriz():
    for i in range(4):
        jogo.append([])
        apostas.append([])
        for _ in range(4):
            num = random.randint(0, len(figuras)-1)
            jogo[i].append(figuras[num])
            apostas[i].append("🟥")
            figuras.pop(num)

def mostra_tabuleiro():
    
    os.system("cls")      # limpa a tela
    print("   1   2   3   4")
    for i in range(4):
        print(f"{i+1}", end="")
        for j in range(4):
            print(f" {jogo[i][j]} ", end="")
        print("\n")
    
    print("Memorize a posição dos bichos...")
    time.sleep(2)

    print("Contagem regressiva: ", end="")
    for i in range(10, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)

    os.system("cls")

def mostra_cartas_e_acertos():
    os.system("cls")      # limpa a tela
    print("   1   2   3   4")
    for i in range(4):
        print(f"{i+1}", end="")
        for j in range(4):
            print(f" {apostas[i][j]} ", end="")
        print("\n")


preenche_matriz()
mostra_tabuleiro()

def aposta_coordenada(num):
    while True:
        mostra_cartas_e_acertos()
        posicao = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
        if len(posicao) != 2:
            print("Informe uma dezena, por exemplo, 12, 24, 31, ...")
            time.sleep(2)
            continue       # volta ao início da repetição
        x = int(posicao[0])-1           # "34"
        y = int(posicao[1])-1
        try:
            if apostas[x][y] == "🟥":
                apostas[x][y] = jogo[x][y]
                break
            else:
                print("Coordenada já apostada...")
                time.sleep(2)
        except IndexError:
            print("Erro... Coordenada inválida")
            time.sleep(2)        
    return x, y

def verifica_vencedor():
    contador = 0
    for i in range(4):
        for j in range(4):
            if apostas[i][j] == "🟥":
                contador += 1
    return contador

# ------------------------ Código do Programa Principal
while True:
    tempo_inicial = time.time()
    x1, y1 = aposta_coordenada(1)
    x2, y2 = aposta_coordenada(2)
    mostra_cartas_e_acertos()

    if apostas[x1][y1] == apostas[x2][y2]:
        print("Parabéns! Você acertou! 😉")
        total_pontos += 10
        cartas_viradas = verifica_vencedor()
        if cartas_viradas == 0:
            print("Parabéns! Você venceu! 🏆🏆")
            break
        else:
            print(f"Falta(m) {cartas_viradas//2} bichos para descobrir")    
            time.sleep(2)        
    else:
        print("Errou... Tente novamente. 😡")
        total_pontos -= 5
        apostas[x1][y1] = "🟥"
        apostas[x2][y2] = "🟥"
        
        continuar = input("Deseja continuar (S/N): ").upper()
        if continuar != "S":
            print("Ah... Você perdeu essa... 🤔")
            break

tempo_final = time.time()
duracao_jogo = tempo_final - tempo_inicial

print()
print("*"*40)
print(f"Jogador: {nome_jogador}")
print(f"Total de Pontos: {total_pontos}")
print(f"Duração do Jogo: {int(duracao_jogo)} segundos")
print("*"*40)

# ----- Rotina para salvar os dados no arquivo ranking.txt
dados = []
if os.path.isfile("ranking.txt"):
    with open("ranking.txt", "r") as arquivo: # "r" -> especifica que é pra leitura, tem no slide
        dados = arquivo.readlines()

# Adiciona uma linha no vetor Dados.
dados.append(f"{nome_jogador};{total_pontos};{int(duracao_jogo)}\n")

# Utilização do with open: ele insere os arquivos e depois fecha totalmente o .txt
with open("ranking.txt", "w") as arquivo:
    for dado in dados:
        arquivo.write(dado)

# ---- Rotina para classificar (ranking)
nomes = []
pontos = []
tempos = []

for dado in dados:
    partes = dado.split(";")
    nomes.append(partes[0])
    pontos.append(int(partes[1]))
    tempos.append(int(partes[2])*-1)

# coloca as 3 listas em ordem (zipando as 3 listas)
juntas = sorted(zip(pontos, tempos, nomes), reverse=True)
# volta a separar as listas (faz um "unzip")
pontos2, tempos2, nomes2 = zip(*juntas)

print()
print("="*40)
print("---------< RANKING DOS JOGADORES >---------")
print("="*40)
print("Nº Nome do Jogador.........: Pontos Tempo.:")

# Função enumerate do python: gera numero de acordo com os dado
# O número do emunerate vai para primeira variavel

for num, (nome, ponto, tempo) in enumerate(zip(nomes2, pontos2, tempos2), start=1):
    if nome == nome_jogador and ponto == total_pontos:
        # 2d indica que é um número inteiro, 25s string
        print(Fore.RED + f"{num:2d} {nome:25s}  {ponto:2d}  {tempo*-1:3d}seg", end="")
        print(Style.RESET_ALL)
    else:
        print(f"{num:2d} {nome:25s}  {ponto:2d}  {tempo*-1:3d}seg")
# ------------------------------------------------------
# Exercícios:
# 1. Solicitar nome do usuário no início do jogo
# 2. Definir uma pontuação para acertos (+10) e erros (-5)
# 3. Obter data e hora do início e final do jogo, mostrar duração
# 4. No final, mostrar a pontuação obtido pelo jogador e tempo
# 5. Salvar nome, pontuação e duração em arquivo texto
# 6. Classificar e mostrar ranking