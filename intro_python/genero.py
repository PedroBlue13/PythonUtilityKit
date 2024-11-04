#Receba F para feminino e M para masculino e exiba a resposta


genero = input('Digite "F" para Feminino e "M" para Masculino: ').strip().upper()
while genero not in ["F", "M"]:
    print("Entrada inválida. Digite apenas 'F' ou 'M'.")
    genero = input('Digite "F" para Feminino e "M" para Masculino: ').strip().upper()

if genero == 'F':
    print("F selecionado.")
elif genero == 'M':
    print("M selecionado")

