import time

print("[--- INICIANDO SIMULACIÓN DE FUERZA BRUTA PARA LOGIN ---]\n")

# Simulamos que conocemos el usuario correcto pero no la clave
usuario_objetivo = "administrador"

# Nuestro diccionario de contraseñas de prueba (la contraseña real es "secreto123")
diccionario_passwords = [
    "123456",
    "password",
    "admin123",
    "hola123",
    "secreto123",
    "qwerty"
]

acceso_concedido = False

for intento in diccionario_passwords:
    print(f"Probando contraseña para '{usuario_objetivo}': {intento}")
    
    # Simulamos el tiempo de respuesta del servidor (pequeña pausa)
    time.sleep(0.5)
    
    if intento == "secreto123":
        print(f"\n[¡CONTRASEÑA ENCONTRADA!] -> ¡La clave es: '{intento}'!")
        acceso_concedido = True
        break
    else:
        print("    [-] Acceso denegado (Credenciales incorrectas)")

if not acceso_concedido:
    print("\n[-] El diccionario se agotó y no se encontró la contraseña.")
else:
    print("\n[+] ¡Ataque de fuerza bruta simulado con éxito! Sesión iniciada.")