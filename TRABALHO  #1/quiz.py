import random
import time
import os
import csv
from colorama import Fore, Back, Style

perguntas = []

with open("perguntas.csv", mode="r", encoding="utf-8") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        perguntas.append(linha)

nome_jogador = input("Insira seu nome: ")
pontos = 0
questao = ""

def gerar_pergunta():
    print(f"Atenção para a pergunta, {nome_jogador}!")
    time.sleep(2)
    for i in range(3, 0, -1):  # contagem regressiva de 3 seg
        print(i,flush=True)    # p/ imprimir a pergunta
        time.sleep(1)
        os.system("cls")
    global questao
    questao = random.choice(perguntas) 
    
def dados_jogador():
    print("-"*30)
    print(f"Jogador: {nome_jogador}")
    print(f"Pontuação Final: {pontos}")
    print(f"Tempo de Jogo: {int(duracao):.2f}")
    print("-"*30)

gerar_pergunta()
while True:
    print(questao["pergunta"])
    print(f"A) {questao["opcaoA"]}")
    print(f"B) {questao["opcaoB"]}")    
    print(f"C) {questao["opcaoC"]}")
    print(f"D) {questao["opcaoD"]}")

    inicio = time.time()
    resposta = input("Escolha uma opção (A, B, C, D): ").upper()

    if resposta in ("A", "B", "C", "D"):
        if resposta == questao["resposta"]:
            print(Fore.GREEN+"Parabéns você acertou!")
            print(Style.RESET_ALL)
            pontos += 10
            gerar_pergunta()
        else:
            print(Fore.RED+"Resposta Errada você perdeu...")
            print(Style.RESET_ALL)
            time.sleep(2)
            os.system("cls")
            final = time.time()
            duracao = final - inicio
            dados_jogador()
            break
    else:
        print(Fore.YELLOW+"Insira uma resposta válida (A, B, C, D). ")
        print(Style.RESET_ALL)
        time.sleep(2)
        os.system("cls")



## salvar dados 

dados = []
if os.path.isfile("ranking.txt"):
    with open("ranking.txt", "r") as arquivo: 
        dados = arquivo.readlines()

dados.append(f"{nome_jogador};{pontos};{duracao}\n")

with open("ranking.txt", "w") as arquivo:
    for dado in dados:
        arquivo.write(dado)

## Ranking

while True:
    ranking = input("Deseja ver o ranking geral de jogadores? (S/N)").upper()
    if ranking in "S":
        nomes = []
        pontos = []
        tempos = []

        for dado in dados:
            partes = dado.split(";")
            nomes.append(partes[0])
            pontos.append(int(partes[1]))
            tempos.append(float(partes[2]))
        
        juntas = sorted(zip(pontos, tempos, nomes), key=lambda x: (-x[0], x[1]))
        
        ## AJUSTAR OPÇOES DAS PERGUNTAS 

        ##-------- CABEÇALHO DA TABELA
        print(f"{'N°':<8}{'Jogador':<35}{'Pontos':<8}{'Tempo (s)':<10}")
        print("="*60)

        ##--------- ENTENDER ISSO 
        pontos2, tempos2, nomes2 = zip(*juntas)
        for num, (nome, ponto, tempo) in enumerate(zip(nomes2, pontos2, tempos2), start=1):
            if nome == nome_jogador:
                print()
                print(Fore.CYAN + f"{num:<8}{nome:<35}{ponto:<8}{tempo:<10.2f}")
                print(Style.RESET_ALL)
            else:
                print(f"{num:<8}{nome:<35}{ponto:<8}{tempo:<10.2f}")
        break
    else:
        break
