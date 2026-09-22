import urllib.request
import urllib.error

# Objetivo simulado de prueba
url_objetivo = "http://scanme.nmap.org"

# Diccionario de rutas comunes que un Red Teamer busca en un servidor web
diccionario_rutas = [
    "admin",
    "login",
    "dashboard",
    "backup.zip",
    "config.php",
    "server-status",
    "api/v1",
    "secretos"
]

print(f"--- INICIANDO FUZZING DE DIRECTORIOS EN: {url_objetivo} ---")

for ruta in diccionario_rutas:
    url_completa = f"{url_objetivo}/{ruta}"
    try:
        # Hacemos la petición web a cada ruta del diccionario
        respuesta = urllib.request.urlopen(url_completa, timeout=3)
        print(f"[¡ENCONTRADO!] Ruta activa: /{ruta} (Código: {respuesta.getcode()})")
    except urllib.error.HTTPError as e:
        # Si el servidor responde con un 403 (Prohibido), ¡la ruta existe pero está protegida! (Oro puro para un Red Team)
        if e.code == 403:
            print(f"[PROTEGIDO/EXISTE] /{ruta} - Código 403 (Acceso denegado, vale la pena investigar)")
        else:
            # Si da 404 (No encontrado), el directorio no existe
            pass
    except Exception:
        # Ignoramos errores de conexión genéricos para que el script fluya rápido
        pass

print("\n--- Fuzzing finalizado ---")