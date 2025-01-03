

pokemon = []
while True:
    nome = input("Digite Blue para sair ou cadastre um pokemon: \n")
    if nome == "Blue":
        break
    
    pokemon.append(nome)
pokemon.sort()
print(pokemon)