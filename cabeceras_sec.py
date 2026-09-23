import urllib.request
import urllib.error

# Definimos nuestro objetivo de estudio
objetivo = "http://scanme.nmap.org"

print(f"\n[--- ANALIZANDO CABECERAS DE SEGURIDAD EN: {objetivo} ---]\n")

try:
    req = urllib.request.Request(objetivo, headers={'User-Agent': 'Mozilla/5.0 (RedTeam-Student)'})
    with urllib.request.urlopen(req, timeout=5) as respuesta:
        # Obtenemos todas las cabeceras HTTP que responde el servidor
        cabeceras = respuesta.headers
        
        print(f"Estado de la conexión: {respuesta.status} {respuesta.reason}\n")
        print("[+] Cabeceras encontradas en el servidor:")
        for clave, valor in cabeceras.items():
            print(f"    - {clave}: {valor}")
            
        print("\n[--- AUDITORÍA DE CABECERAS CRÍTICAS ---]")
        # Cabeceras de seguridad clave que un servidor blindado debería tener:
        cabeceras_clave = [
            'Content-Security-Policy', 
            'X-Frame-Options', 
            'X-XSS-Protection', 
            'Strict-Transport-Security'
        ]
        
        for ch in cabeceras_clave:
            if ch in cabeceras:
                print(f"  [SEGURO] Presente -> {ch}")
            else:
                print(f"  [ALERTA/VULNERABLE] Falta la cabecera -> {ch}")

except urllib.error.URLError as e:
    print(f"[!] Error al conectar con el objetivo: {e.reason}")

print("\n[--- ANÁLISIS FINALIZADO ---]")