
sum = 0
y = 0

x = []
for b in range(4):
    num = int(input(f"Tentativa {b + 1}/4 - Digite um número para somar: "))
    x.append(num)
    print(f"Você digitou {b + 1} número(s), faltam {3 - b}.")
     
for delta in x:
    sum += delta

print(f"A soma dos números digitados é: {sum}")