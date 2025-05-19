# 6. Elabore um programa de implemente um
# jogo de Craps, conforme descrição a seguir: O
# jogador lança um par de dados (2 números
# aleatórios entre 1 e 6), obtendo um valor entre
# 2 e 12. Se, na primeira jogada, você tirar 7 ou
# 11, você tirou um "natural" e ganhou. Se você
# tirar 2, 3 ou 12 na primeira jogada, isto é
# chamado de "Craps" e você perdeu. Se, na
# primeira jogada, você fizer um 4, 5, 6, 8, 9 ou
# 10, este é o seu "Ponto". Seu objetivo agora é
# continuar jogando os dados até tirar este
# número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este "Ponto" novamente.
import random
import time

nome = input("Nome do Jogador: ")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
soma = dado1 + dado2

print(f"1° Dado Sorteado: {dado1}", flush=True)
time.sleep(1)
print(f"2° Dado Sorteado: {dado2}", flush=True)
time.sleep(1)
print(f"Seu número é {soma}")

if soma == 7 or soma == 11:
    print(f"{nome} você ganhou!")
elif soma == 2 or soma == 3 or soma == 12:
    print(f"{nome}, CRAPS! Você perdeu...")
else:
    ponto = soma
    print(f"{nome}, {soma} é seu ponto, seu objetivo é tirar este número novamente.")
    print("Caso tire o número 7 antes, você perde.")

    while True:
        print("-"*30)
        input("Pressione Enter para jogar os dados.")

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2

        print(f"1° Dado Sorteado: {dado1}", flush=True)
        time.sleep(1)
        print(f"2° Dado Sorteado: {dado2}", flush=True)
        time.sleep(1)
        print(f"Seu número é {soma}")

        if soma == ponto:
            print(f"Parabéns {nome}, você ganhou!")
            break
        elif soma == 7:
            print(f"{nome}, você perdeu.")
            break
        
    


    
