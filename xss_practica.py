# Simulación de un sistema de comentarios vulnerable a XSS
def mostrar_comentario_en_web(comentario):
    print(f"\n[+] El usuario escribe en la web: {comentario}")
    
    # Si la web es insegura y 'refleja' el texto sin limpiar, interpreta etiquetas HTML/JS
    if "<script>" in comentario:
        print("[!] ¡ALERTA DE SEGURIDAD (XSS)!")
        print("[!] El navegador web ejecutó el código malicioso del atacante:")
        print(f"    --> [EJECUCIÓN MALICIOSA]: {comentario}")
        print("    --> (Impacto real: Robo de cookies de sesión o redirección a sitios phishing).")
    else:
        print(f"[OK] Comentario seguro mostrado correctamente: {comentario}")

# Prueba 1: Comentario normal de un usuario legítimo
mostrar_comentario_en_web("Hola a todos, muy buena la página.")

# Prueba 2: Comentario con carga útil (Payload) XSS
mostrar_comentario_en_web("<script>alert('¡Robé tu sesión!');</script>")