def contagem(n):
    if n == 0:
        print("FIM!")
    else:
        print(f"{n}!")
        contagem(n-1)

contagem(5)

for i in range(5, 0, -1):
    print(i)
print("Fim")