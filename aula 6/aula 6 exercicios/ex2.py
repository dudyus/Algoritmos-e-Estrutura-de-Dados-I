# 2. Dada uma lista de nomes, crie novas listas com: a) os nomes em maiúsculas; b) os nomes com apenas as
# primeiras letras do nome em maiúsculas.
# o nomes = ["ana júlia", "joão antônio", "luis eduardo", "maria helena"]
# o nomes2 = ["ANA JÚLIA", "JOÃO ANTÔNIO", "LUIS EDUARDO", "MARIA HELENA"]
# o nomes3 = ["Ana Júlia", "João Antônio", "Luis Eduardo", "Maria Helena"]

nomes = ["ana júlia", "joão antônio", "luis eduardo", "maria helena"]
print(nomes)

nomes2 = [nome.upper() for nome in nomes]
print(nomes2)

nomes3 = 