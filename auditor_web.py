import urllib.request
import urllib.error

# URL objetivo de pruebas (puedes cambiarla por otra que tengas permiso de auditar)
url = "http://scanme.nmap.org"

print(f"--- ANALIZANDO CABECERAS DE SEGURIDAD EN: {url} ---")

try:
    # Hacemos la petición web
    respuesta = urllib.request.urlopen(url)
    headers = respuesta.headers

    # Cabeceras críticas de seguridad que un Red Team siempre busca
    cabeceras_seguridad = [
        "X-Frame-Options",
        "X-XSS-Protection",
        "Content-Security-Policy",
        "Strict-Transport-Security"
    ]

    print("\n[i] Resultados de la auditoría de cabeceras:")
    for cabecera in cabeceras_seguridad:
        if cabecera in headers:
            print(f"  [PROTEGIDO] Encontrada '{cabecera}': {headers.get(cabecera)}")
        else:
            print(f"  [¡VULNERABLE/FALTA!] No se encontró '{cabecera}'")

except urllib.error.URLError as e:
    print(f"[!] Error al conectar con el objetivo: {e}")