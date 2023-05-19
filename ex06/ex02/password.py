import hashlib
import string
import random

def convertir_password(password):
    # Verificar si el password cumple con los requisitos
    if len(password) < 6 or len(password) > 12:
        return None
    
    # Generar una semilla aleatoria
    semilla = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    # Concatenar la semilla y el password
    cadena = semilla + password
    
    # Calcular el hash MD5 de la cadena
    hash_md5 = hashlib.md5(cadena.encode()).hexdigest()
    
    # Devolver los primeros 32 caracteres del hash como resultado
    return hash_md5[:32]