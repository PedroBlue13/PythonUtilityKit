#Receba e verifique entre 3 numeros qual é o maior

n1 = int(input("digite um número: "))
n2 = int(input("digite o segundo número: "))
n3 = int(input("digite o terceiro número: "))


numeros = [n1, n2, n3]

maior_numero = max(numeros)



if numeros.count(maior_numero) == 3:
    print("Todos os números são iguais.")
elif numeros.count(maior_numero) == 2:
    print(f"Os maiores números são iguais a {maior_numero}")
else:
    print(f"O maior número é {maior_numero}.")