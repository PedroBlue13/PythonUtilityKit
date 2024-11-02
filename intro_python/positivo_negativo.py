#Receba um número e exiba se ele é positivo ou negativo



numero = float(input("digite um número: "))


if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('Esse número só pode ser zero!')