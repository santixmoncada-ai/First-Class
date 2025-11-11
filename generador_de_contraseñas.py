import random 

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

cantidad = int(input("cuantos caracteres hay?"))

password = "" 

for i in range(cantidad):
    password += random.choice(caracteres) 
    
print(password)  
