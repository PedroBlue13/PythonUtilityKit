#Receba um número e mostre todos os números pares de 0 até número digitado

while True:
        try:
             n1 = int(input("Digite um número para contarmos todos os números pares até ele:\n"))
             break
        except ValueError:
            print("Apenas números inteiros são aceitos!") 
            
linha = 1      
i = 1
while i <= n1:    
    if i % 2 == 0:
        print(f'Linha: {linha} número: {i}')
        linha +=1
    i +=1
print(f'Foram contadas "{linha-1}" linhas para chegar até "{i-1}"')