# Lista de carpetas que queremos adivinar
diccionario_rutas = ["admin", "login", "dashboard", "secretos"]

print("--- INICIANDO SIMULACIÓN DE FUZZING ---")

for ruta in diccionario_rutas:
    # Simulamos que probamos cada ruta
    print(f"Probando la ruta: /{ruta}")
    
    # Imaginemos que la ruta 'admin' dio un Match exitoso
    if ruta == "admin":
        print(f"[¡MATCH EXITOSO!] ¡Directorio descubierto! /{ruta} (Código HTTP: 200 OK)")
    else:
        print(f"[-] No encontrada (Código HTTP: 404)")

print("\n--- Fuzzing finalizado ---")