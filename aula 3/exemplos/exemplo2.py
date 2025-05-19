cidade = input("Cidade: ") # Santa Vitória do Palmar

partes = cidade.split(" ")

print(f"1º nome da cidade: {partes[0]}")    # partes[0] = "Santa"
                                            # partes[1] = "Vitória"
                                            # partes[2] = "do"
                                            # partes[3] = "Palmar"

for parte in partes:
    print(parte)