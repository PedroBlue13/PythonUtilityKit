#receba a nota do aluno valores entre 0 e 10

cabrito = 2

while True:
    try:
        nota = int(input("Digite a nota do aluno:\n"))
        if nota >= 0 and nota <= 10:
            print(f"A Nota '{nota}'. Foi salva com sucesso! ")
            break
        else:
            print("A nota deve estar entre 0 e 10. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.") 