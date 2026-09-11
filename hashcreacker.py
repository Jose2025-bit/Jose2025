import hashlib

hash_file = "75n45c737535097n77474c7457c4nmxnc7vcmx757xn"

with open(dic_file, 'r') as file:
    diccionario = [line.strip() for line in file]
    
    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        
        if hash_calculado == hash_file:
            
            print("la contrasena original es: " + password)
            break
        else:
            print("la contrasena no se encuentra en el diccionario")
            