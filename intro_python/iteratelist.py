#forma não pythonica 

dias = [1,3,2,5,7,6]

for i in range(0, len(dias)):
    print(dias[i], i)
    print(f'Dia: {dias[i]} Posição: {i}')
    
    
#forma pythonica
for i in dias:
    print(i)
    
#mais pythonica ainda
x = list(enumerate(dias)) 
print(f'valor de x{x}')   