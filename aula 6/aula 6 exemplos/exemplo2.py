x = 10 
y = 20

def teste():
    global x # sem o global x = 5 apenas dentro da função teste
    x = 5
    print(x)
    print(y)

teste()
print(x)
print(y)