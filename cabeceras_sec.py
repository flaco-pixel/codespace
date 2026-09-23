# Simulador de auditoría de cabeceras HTTP de seguridad

def auditar_cabeceras(url_objetivo, cabeceras_servidor):
    print(f"\n[+] Auditando la seguridad de: {url_objetivo}")
    
    # Cabeceras críticas que todo servidor seguro deberia tener
    cabeceras_requeridas = [
        "Content-Security-Policy",     # Frena ataques XSS e inyecciones
        "X-Frame-Options",            # Frena ataques de Clickjacking
        "X-Content-Type-Options",     # Evita que el navegador adivine tipos de archivos maliciosos
        "Strict-Transport-Security"   # Fuerza el uso exclusivo de HTTPS
    ]
    
    for cabecera in cabeceras_requeridas:
        if cabecera in cabeceras_servidor:
            print(f"  [SEGURO] Encontrada: {cabecera}")
        else:
            print(f"  [PELIGRO] FALTA LA CABECERA: {cabecera} (Vulnerable)")

# --- PRUEBA 1: Servidor mal configurado (Inseguro) ---
servidor_inseguro = {
    "Server": "Apache/2.4.7",
    "Content-Type": "text/html"
    # ¡Faltan todas las cabeceras de seguridad!
}
auditar_cabeceras("http://sitio-vulnerable.com", servidor_inseguro)

# --- PRUEBA 2: Servidor bien configurado (Seguro) ---
servidor_seguro = {
    "Server": "Apache/2.4.7",
    "Content-Type": "text/html",
    "Content-Security-Policy": "default-src 'self'",
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Strict-Transport-Security": "max-age=31536000"
}
auditar_cabeceras("http://sitio-seguro.com", servidor_seguro)