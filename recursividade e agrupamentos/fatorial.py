def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

calc = (fatorial(5))
print(f"Fatorial de 5: {calc}")

total = 1
for i in range(5, 0, -1):
    total = total * i

print(f"Fatorial do 5: {total}")