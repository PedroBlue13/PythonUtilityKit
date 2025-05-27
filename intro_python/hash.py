import hashlib


while True:
    try:
        password = input("Digite uma senha:\n")
        if len(password) >=2: 
            print("Senha cadastrada com sucesso!")
            break
        else:
            print("A senha deve ser maior que 2 digitos.")

    except Exception as e:
            print(f"Algo de errado aconteceu, erro: {e}")
        

bytes_pass = bytes(password, encoding="UTF-8")
hash_pass = hashlib.sha256(bytes_pass).hexdigest()

print(f'Hash da senha: {hash_pass}')
            
