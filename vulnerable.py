import sqlite3

# 1. Creamos una base de datos falsa en memoria RAM con un usuario registrado
conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, password TEXT)")
# Insertamos un usuario legítimo: admin / Secreto123
cursor.execute("INSERT INTO usuarios (usuario, password) VALUES ('admin', 'Secreto123')")
conexion.commit()

def login_inseguro(usuario_ingresado, password_ingresado):
    # ¡EL ERROR GRAVE DE PROGRAMACIÓN! Concatenar variables directamente en el SQL
    # Un atacante puede manipular la variable 'usuario_ingresado'
    consulta = f"SELECT * FROM usuarios WHERE usuario = '{usuario_ingresado}' AND password = '{password_ingresado}'"
    
    print(f"\n[DEBUG] Consulta SQL ejecutada: {consulta}")
    
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    
    if resultado:
        print("  [ACCESO CONCEDIDO] ¡Bienvenido al sistema!")
    else:
        print("  [ACCESO DENEGADO] Credenciales incorrectas.")

# --- PRUEBA 1: Login normal (Fallaría si pones mal la contraseña) ---
print("--- PRUEBA 1: Intento normal con contraseña errónea ---")
login_inseguro("admin", "contraseña_falsa")

# --- PRUEBA 2: INYECCIÓN SQL (El ataque) ---
print("\n--- PRUEBA 2: Inyección SQL (Bypasseando el login sin saber la contraseña) ---")
# ¿Qué pasa si ingresamos este texto malicioso como usuario?
payload_malicioso = "admin' --"
login_inseguro(payload_malicioso, "cualquier_cosa")