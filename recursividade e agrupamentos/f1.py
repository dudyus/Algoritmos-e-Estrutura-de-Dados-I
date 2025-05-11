import csv

ganhadores = []

with open("winners.csv", mode="r", encoding="utf-8") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        ganhadores.append(linha)

def mais_vitorias():  #decrescente
    grupo = {}
    for ganhador in ganhadores:
        piloto = ganhador["Winner"]
        grupo[piloto] = grupo.get(piloto, 0) + 1
        print(grupo)

mais_vitorias()