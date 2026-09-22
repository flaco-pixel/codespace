import socket

# Definimos el objetivo (por ahora localhost o tu propia máquina de prueba)
objetivo = "127.0.0.1"
puertos = [21, 22, 80, 443, 8080]

print(f"--- ESCANEANDO OBJETIVO REAL: {objetivo} ---")

for puerto in puertos:
    # Creamos un socket de tipo IPv4 (AF_INET) y TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) # Tiempo de espera de 1 segundo
    
    # Intentamos conectar al puerto
    resultado = s.connect_ex((objetivo, puerto))
    
    if resultado == 0:
        print(f"[+] El puerto {puerto} esta ABIERTO")
    else:
        print(f"[-] El puerto {puerto} esta cerrado")
        
    s.close()