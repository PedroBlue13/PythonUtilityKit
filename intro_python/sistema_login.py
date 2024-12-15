#Defina um usuario e senha 
#verifique se login do usuario é valido


user = "usuario"
senha = "password"


while True:
        usern = input("Digite seu nome de usuário:\n")
        passw = input("Digite sua senha:\n")
        if usern == user and passw == senha:
            print(f'Você está logado como: {user} ')
            break
        else:
             print("Digite usuário e senha validos!") 