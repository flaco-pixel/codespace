import socket
import time

# 1. Definimos el objetivo (usamos localhost para pruebas seguras)
objetivo = "127.0.0.1"

print(f"--- COMENZANDO ESCANEO AUTOMATIZADO EN: {objetivo} ---")
inicio = time.time()

# 2. Bucle para recorrer automáticamente los puertos del 1 al 100
for puerto in range(1, 101):
    # Creamos el socket IPv4 y TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)  # Timeout corto para agilizar el escaneo
    
    # Intentamos la conexión al puerto actual del bucle
    resultado = s.connect_ex((objetivo, puerto))
    
    # Si el resultado es 0, significa que el puerto está abierto
    if resultado == 0:
        print(f"[+] ¡Puerto ABIERTO encontrado! -> Puerto {puerto}")
    
    # Cerramos el socket para liberar memoria
    s.close()

fin = time.time()
print(f"--- ESCANEO FINALIZADO EN {fin - inicio:.2f} segundos ---")