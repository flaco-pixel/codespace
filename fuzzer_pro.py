import urllib.request
import urllib.error

# Definimos el objetivo (usaremos un sitio web seguro de pruebas)
objetivo = "http://scanme.nmap.org"

# Nuestro "diccionario" o listado de palabras clave a buscar en el servidor
diccionario_rutas = [
    "admin",
    "login",
    "images",
    "server-status",
    "backup",
    "secret",
    "api",
    "config.json"
]

print(f"\n[--- INICIANDO FUZZING PROFESIONAL EN: {objetivo} ---]\n")

for ruta in diccionario_rutas:
    url_completa = f"{objetivo}/{ruta}"
    try:
        # Intentamos hacer una petición HTTP GET a la ruta
        req = urllib.request.Request(
            url_completa, 
            headers={'User-Agent': 'Mozilla/5.0 (RedTeam-Student)'}
        )
        with urllib.request.urlopen(req, timeout=3) as respuesta:
            codigo = respuesta.getcode()
            if codigo == 200:
                print(f"[¡ENCONTRADO! - 200 OK] -> {url_completa}")
            else:
                print(f"[Código {codigo}] -> {url_completa}")
                
    except urllib.error.HTTPError as e:
        # Si da 404 (No encontrado), el servidor responde con error, lo filtramos o mostramos de forma limpia
        if e.code == 404:
            # print(f"[-] No existe: {url_completa}") # Comentado para no ensuciar la terminal
            pass
        else:
            print(f"[!] Error HTTP {e.code} en: {url_completa}")
    except Exception:
        # Ignoramos errores de conexión genéricos para que el script no se caiga
        pass

print("\n[--- FUZZING FINALIZADO CON ÉXITO ---]")