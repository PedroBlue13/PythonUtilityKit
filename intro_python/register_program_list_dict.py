
#Crie um programa em Python para gerenciar uma lista de pessoas. O programa deve permitir que o usuário cadastre várias pessoas, armazenando o nome e a idade de cada uma em um dicionário. Esses dicionários devem ser adicionados a uma lista


peoples = []


while True:
    decision = int(input('enter 1 to register 2 to exit\n'))
    if decision == 2:
        break
    
    
    people = { 'name': input('enter the name: \n'),
                'age': input('enter the age: \n')
    }
    
    peoples.append(people)
    
    
for i in peoples:
    print(i)