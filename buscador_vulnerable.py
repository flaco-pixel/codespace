# Simulando una base de datos de productos en una tienda online
productos_tienda = {
    "campera": "Campera de abrigo - Stock: 15 - Precio: $50",
    "zapatillas": "Zapatillas deportivas - Stock: 8 - Precio: $80",
    "gorra": "Gorra urbana - Stock: 30 - Precio: $20"
}

def buscador_inseguro(termino_busqueda):
    print(f"\n[+] Buscando producto con el término: '{termino_busqueda}'")
    
    # Simulamos cómo armaría la consulta SQL el sistema vulnerable
    # Si el usuario ingresa texto malicioso, romperá esta estructura lógica
    consulta_sql = f"SELECT * FROM productos WHERE nombre = '{termino_busqueda}'"
    print(f"    (Consulta interna ejecutada): {consulta_sql}")
    
    # Lógica simulada de la inyección
    if "OR 1=1" in termino_busqueda or "--" in termino_busqueda:
        print("\n[!] ¡ALERTA DE SEGURIDAD! Inyección SQL detectada.")
        print("[!] El sistema ignoró el filtro y devolvió TODO el catálogo:")
        for clave, valor in productos_tienda.items():
            print(f"    -> {valor}")
    elif termino_busqueda in productos_tienda:
        print(f"[EXITO] Producto encontrado: {productos_tienda[termino_busqueda]}")
    else:
        print("[-] Producto no encontrado.")

# --- PRUEBA 1: Búsqueda normal ---
buscador_inseguro("campera")

# --- PRUEBA 2: Búsqueda maliciosa (Inyección SQL) ---
buscador_inseguro("' OR 1=1 --")