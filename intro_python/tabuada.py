#Receba um número do usuário e  mostre a  tabuada desse número



comparator = 200
list =["counter +=1", "comparator -=200"] 

# Solicita um número ao usuário
while True:
    try:
        numero = int(input("Digite um número inteiro!\n"))
        break  # Sai do loop se o número for válido
    except ValueError: 
        print("Entrada inválida! Por favor, digite um número inteiro.")

# Inicializa as variáveis
counter = 0
max_value = numero * 10

print(f'O número máximo da tabuada do {numero} é {max_value}')

# Gera a tabuada
while counter <= 10:  # Ajustado para mostrar a tabuada até 10
    multiply = numero * counter
    print(f'{numero} x {counter} = {multiply}')
    counter += 1