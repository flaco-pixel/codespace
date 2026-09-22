import socket
import time

# 1. Definimos el objetivo (tu localhost de prueba)
objetivo = "45.33.32.156" # IP de scanme.nmap.org

# 2. Podemos definir una lista de puertos o usar un rango automático (ej. del puerto 1 al 100)
print(f"--- COMENZANDO ESCANEO EN: {objetivo} ---")
inicio = time.time()

# Usamos un bucle for para recorrer los puertos del 1 al 100
for puerto in range(1, 101):
    # Creamos el socket IPv4 y TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Un tiempo de espera corto para que sea más rápido
    
    # Intentamos conectar al puerto actual del bucle
    resultado = s.connect_ex((objetivo, puerto))
    
    if resultado == 0:
        print(f"[+] El puerto {puerto} está ABIERTO")
    
    # Cerramos el socket para liberar recursos
    s.close()

fin = time.time()
print(f"--- ESCANEO FINALIZADO EN {fin - inicio:.2f} segundos ---")