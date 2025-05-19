import time
import random

nome = input("Nome do Apostador: ")
valor = float(input("Valor da Aposta R$: "))

input("Pressione Enter para iniciar o sorteio...")
print()

figuras = "🍀🐯🎈"
jogo = ""

print("Suas Apostas: ", end="")

for _ in range(3): # Loop que repete 3 vezes
    # Gera um nº aleatório entre 0.. 2
    num = random.randint(0, 2)
    print(figuras[num], end=" ", flush=True) # O flush permite que vá aparecendo os emojis de 1 em 1 segundo utilizando o time.sleep
    time.sleep(1)
    jogo = jogo + figuras[num]
    
print()
if jogo[0] == jogo[1] and jogo[1] == jogo[2]:
    print(f"Parabéns {nome}, você ganhou R${valor*3:6.2f}! 🎉")
elif jogo[0] == jogo[1] or jogo[0] == jogo[2] or jogo[1] == jogo[2]:
    print(f"Foi por pouco {nome}....")
else:
    print("Não foi dessa vez.")