import requests

while True:
    try:
            number = int(input("Digite um número inteiro para seu pokemon na pokedex.\n1"))
            break
    except ValueError:
        print("Digite apenas numeros inteiros!")

url = f"https://pokeapi.co/api/v2/pokemon/{number}"



try:
    api = requests.get(url)
    data = api.json()
    pokemon = data["name"], data["types"]

    print(f"Pokemon: {pokemon[0]} \n Types:{pokemon[1][0]['type']['name']}")
except Exception as e:
    print(f"Algo de estrango ocorreu. erro {e}")

