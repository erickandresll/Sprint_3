'''

La aplicación es para la generación de usuarios con contraseña para clientes de empresas 
que solicitan recurso humano externo. La contraseña se genera aleatoriamente desde un comienzo
como método de seguridad.  

'''
# Se importa libreria random para crear contraseñas aleatorias.

import random
import time #Agregué time para que las listas no salieran muy rápidas.

# Se realiza función de crear usuarios, además genera una contraseña aleatoria
# con criterio de que debe contener mayúscula, minúscula y digito. 

def nuevo_cliente(usuario):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #Se agregan todos los carácteres y digitos necesarios en una variables.
    clave = "".join(random.choice(caracteres) for i in range(8)) 
    cuenta = (usuario, clave)
    return cuenta

#Usuarios a crear, cuentas y teléfonos a solicitar.
usuarios = ["Sofía García", "Diego Martínez", "Emilio López", "Juan Torres", "Laura Sánchez", "Carlos Hernández", "Isabel Pérez", "Carmen Castro", "Mario Flores", "Luis Rojas"]
cuentas = []
telefonos = {}

#Se realiza un bucle for para recorrer la lista 'usuarios' y solicitar número telefónicos. 
#Cada iteración va creando una cuenta de usuario y guardandolo en lista 'cuentas'.
for usuario in usuarios:
    cuenta = nuevo_cliente(usuario)
    cuentas.append(cuenta)
    telefono = ""
    while len(telefono) != 8: #El bucle while se va ejecutando hasta que todo los usuarios con cuenta creada tengan número de teléfono.
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        if len(telefono) != 8: #Se insiste en que debe tener 8 digitos.
            print("El número telefónico debe tener 8 dígitos.")
    telefonos[usuario] = telefono #Cuando el usuario tiene teléfono valido se agrega al diccionario 'telefono'. 

#Se imprimen los usuarios y contraseña. 

print("USUARIOS Y CONTRASEÑAS CREADAS")
for cuenta in cuentas:
    time.sleep(1)
    print(f"{cuenta[0]}: {cuenta[1]}") #Tupla, el usuario está en el 0 y la contraseña en el 1. 

print("\n")
  
print("NÚMERO TELEFÓNICOS DE LOS USUARIOS")
for usuario, telefono in telefonos.items():
    time.sleep(1)
    print(f"{usuario}: {telefono}")
    
print("\n")