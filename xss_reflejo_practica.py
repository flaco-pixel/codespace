# Simulación de un servidor web vulnerable a XSS Reflejado

def mostrar_comentario(comentario_usuario):
    # Simulamos lo que hace una web insegura: imprime el HTML directamente
    print(f"[WEB] Comentario publicado por el usuario:")
    print(f"<div>{comentario_usuario}</div>")

print("--- PRUEBA 1: Texto normal ---")
mostrar_comentario("¡Hola a todos! Excelente página.")

print("\n--- PRUEBA 2: Inyección de Script Malicioso (XSS) ---")
# ¿Qué pasa si el atacante en vez de texto escribe una etiqueta de JavaScript?
payload_xss = "<script>alert('¡XSS Exitoso! Tu sesión ha sido robada');</script>"
mostrar_comentario(payload_xss)