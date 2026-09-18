print("--- SIMULADOR DE ESCANEO DE RED ---")
objetivo = "192.168.1.1"
puertos = [80, 443, 22, 21]

print(f"Analizando el objetivo: {objetivo}...")
for puerto in puertos:
    print(f"[+] El puerto {puerto} esta abierto en {objetivo}")