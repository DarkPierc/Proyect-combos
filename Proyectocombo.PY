import random
import string
import names
import os
import sys
import time
from collections import Counter
from colorama import init, Fore, Style

init(autoreset=True)

# ---- Banner Personalizable ----
BANNER = f"""{Fore.CYAN}
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣺⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣯⣿⡯⢟⣛⡛⣓⡛⡿⢽⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁
⡅⠳⢢⣔⣽⡝⢻⠿⣿⣿⣿⣿⣿⣿⣻⡻⣿⣿⢿⣿⡼⣿⢭⣿⡓⣺⣭⠽⣿⣳⣿⡷⣿⡿⣟⣻⣻⣿⣿⣿⣿⡿⢟⢟⢹⡭⣔⠔⢎⢈
⡛⠺⡲⢮⢯⡷⣝⣵⣐⢾⣈⢯⠫⡛⢿⣻⣷⢿⣯⡽⣿⣩⡷⣞⣿⢿⣺⢮⣝⣟⢭⢟⢯⣿⣟⢟⠫⣛⢭⣱⢖⣪⣮⡲⣿⢯⠧⠗⠖⢛
⣬⣃⢗⣷⢿⣿⣶⢬⢍⣗⡿⣏⣿⣛⣾⣼⣻⣳⢷⣵⡞⡽⣿⢽⡾⣽⣝⣯⢟⢶⣯⣾⣟⣟⣥⡷⣻⣯⣽⣗⣻⣩⡰⣼⣿⣷⣻⣝⣪⣬
⠤⣬⢹⣯⣟⣿⡿⣛⡿⣻⣳⣺⡮⣿⢾⣟⣽⣿⣗⣷⡿⠿⠿⢿⣯⣯⣗⠿⠿⢿⣾⣻⣿⣻⣻⣿⣿⣵⣖⣮⣿⣻⡛⣿⣟⣾⣞⡭⣡⠄
⣶⣼⣶⣻⣿⣟⢭⡷⢿⡯⠿⠵⠛⣱⣿⠏⢉⠈⠙⣯⣿⠄⠰⣿⣟⣞⣿⡂⠀⣄⡈⠙⣍⡉⠙⢹⣻⣺⣿⠛⠓⣿⡾⣺⣿⣿⣺⣮⣮⣶
⣄⣦⢦⣿⣿⣿⣷⣿⡟⠀⣴⣶⡠⣺⡯⠀⢼⡇⠀⣿⣿⡁⢘⣿⡿⣽⣿⡅⠀⣿⡇⠀⣿⣦⠀⠹⣗⣿⣿⠀⠰⣿⣻⣽⣿⣿⣷⣦⣰⣀
⣶⠮⣯⢾⠾⣫⣿⣿⡇⠀⠛⠿⢿⣿⡯⠀⣺⡇⠀⣿⣿⡂⢨⣿⣯⣾⣿⡆⠀⣿⡇⠀⣿⣿⡦⡀⢯⢿⠇⠀⣽⣟⣿⣟⡟⢷⡽⡮⢶⣶
⣿⠿⠎⡱⡽⣳⣿⣿⣽⣦⣀⡀⠀⢼⣯⠂⣺⡇⢅⣿⣿⡪⣸⣽⣿⣿⣿⡎⡄⣟⣗⣙⡻⡿⣿⡔⡘⣼⠁⣰⣿⡯⣿⡻⣟⣗⢊⠻⢷⣿
⣦⣮⣼⡾⡟⣿⣼⣮⣿⡿⣟⣻⠀⣽⣿⣸⢸⡇⡧⣿⣿⡺⣼⢿⣿⠏⣾⡇⡆⣿⡇⡋⣯⣞⣿⢟⣦⢁⢢⡿⣿⣿⣿⢟⣿⣺⢷⣵⣴⣴
⣿⣿⠿⡙⣿⢿⣽⢃⣿⢸⣯⣻⢐⣽⣷⢽⢸⡗⡝⣯⣿⢈⡚⡛⢉⢨⢿⡩⠆⠿⡇⠅⣿⣷⣻⢾⡏⡎⣞⣿⣷⣯⡻⣟⣼⣷⠛⢿⣿⣿
⢟⣱⣰⣥⢯⣟⣿⠀⢿⢷⣽⠏⢐⣽⣿⢼⡠⡤⣾⣿⢽⠿⢿⠿⢿⡿⡿⢯⣾⣧⣴⣵⣿⢵⣿⣻⣇⢧⢿⣿⣿⣫⣿⣿⢷⣹⣭⣲⣨⣻
⣿⣿⣟⣭⡮⣻⣻⣮⣢⣌⣅⣦⡾⣿⢿⣿⣻⡿⡿⢽⣿⣬⣽⡸⣼⣳⢜⣵⣯⣽⡿⢿⡽⣿⣯⣿⠇⠣⢛⣿⡿⢞⣵⣿⡫⣶⣝⣿⣿⣿
⣿⣿⣿⣛⣴⣵⠳⣻⡿⣾⣟⣿⣾⣿⣿⡿⣗⣿⣽⢿⡾⣽⣽⡻⣶⡶⣻⣹⣽⣳⣿⣿⣽⡿⣽⣿⣷⣷⣎⣷⣿⣟⡿⡜⣽⣔⣹⣿⣿⣿
⣿⣿⣿⣿⡿⣣⣵⣿⣿⡯⣷⣿⣳⡽⣫⣟⣿⣿⣯⢻⣿⡿⣾⡿⣷⣽⡿⣟⣿⣿⣺⣿⣾⣿⢷⣟⣯⣿⣟⣿⣿⣾⣿⣮⣙⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⡿⣿⣏⣿⡗⣿⣷⣿⣟⣿⣿⣾⡿⣿⣿⣺⢝⣿⣺⡇⣻⣿⣿⣿⣟⣿⣿⢽⣷⣽⡷⣿⣟⢿⣿⣻⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡗⣯⣾⣿⣿⣗⣿⣿⣷⣿⣿⣿⣿⢸⡿⡼⣧⣿⣿⣿⣿⣽⣿⢿⡽⣿⣿⣝⢾⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣾⣿⣿⣿⡳⣇⣿⣿⣿⣿⣿⢿⣾⣟⡺⣿⣿⣿⣿⣿⣿⣯⣿⢽⣿⣿⣟⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣯⣿⡏⣿⣿⣿⣿⣿⣿⢿⣿⣗⢕⣿⣿⣿⣷⣿⣿⢿⣿⢽⣿⣾⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣽⣿⡾⣝⣿⣯⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣾⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{Style.RESET_ALL}"""

def mostrar_banner():
    limpiar_pantalla()
    print(BANNER)
    print(f"{Fore.YELLOW}Bienvenido al Generador de Combos (usuario:contraseña)\n{Style.RESET_ALL}")
    time.sleep(1)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def aplicar_formato(texto, formato):
    if formato == 1:
        return texto.upper()
    elif formato == 2:
        return texto.lower()
    else:
        return texto.capitalize()

def barra_progreso(actual, total):
    porcentaje = int((actual / total) * 100)
    if porcentaje % 10 == 0 or actual == total:  # Solo actualiza cada 10%
        sys.stdout.write(f"\r{Fore.CYAN}Generando... {porcentaje}%{Style.RESET_ALL}")
        sys.stdout.flush()
        if actual == total:
            sys.stdout.write("\n")

def generar_lista_nombres(cantidad, formato, incluir_apellido=False):
    nombres = []
    for _ in range(cantidad):
        nombre = aplicar_formato(names.get_first_name(), formato)
        if incluir_apellido:
            apellido = aplicar_formato(names.get_last_name(), formato)
            nombre = f"{nombre}{apellido}".replace(' ', '').replace('_', '')
        nombres.append(nombre)
    return nombres

# --- Funciones generadoras de combinaciones (todas garantizan NO duplicados) ---
def generar_usuario_letras_password_numeros(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        usuario = aplicar_formato(''.join(random.choices(string.ascii_letters, k=8)), formato)
        password = ''.join(random.choices(string.digits, k=8))
        pares.add(f"{usuario}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nombre_password_random(cantidad, formato):
    while True:
        try:
            largo = int(input(f"{Fore.YELLOW}Ingresa la longitud de la contraseña (4-12): {Style.RESET_ALL}"))
            if 4 <= largo <= 12:
                break
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Ingresa un número entre 4 y 12.{Style.RESET_ALL}")
    pares = set()
    while len(pares) < cantidad:
        usuario = aplicar_formato(names.get_first_name(), formato)
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nombre_igual_password(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        nombre = aplicar_formato(names.get_first_name(), formato)
        pares.add(f"{nombre}:{nombre}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nombre_real_password_numeros(cantidad, formato):
    while True:
        try:
            largo = int(input(f"{Fore.YELLOW}Ingresa la longitud de la contraseña (4-12): {Style.RESET_ALL}"))
            if 4 <= largo <= 12:
                break
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Ingresa un número entre 4 y 12.{Style.RESET_ALL}")
    pares = set()
    while len(pares) < cantidad:
        nombre = aplicar_formato(names.get_first_name(), formato)
        apellido = aplicar_formato(names.get_last_name(), formato)
        usuario = f"{nombre}{apellido}".replace(' ', '').replace('_', '')
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_usuario_password_numerico(cantidad, formato):
    while True:
        try:
            largo = int(input(f"{Fore.YELLOW}Ingresa la longitud del usuario y contraseña (4-12): {Style.RESET_ALL}"))
            if 4 <= largo <= 12:
                break
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Ingresa un número entre 4 y 12.{Style.RESET_ALL}")
    pares = set()
    while len(pares) < cantidad:
        usuario = aplicar_formato(''.join(random.choices(string.digits, k=largo)), formato)
        pares.add(f"{usuario}:{usuario}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nombrecompleto_password_num(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        nombre = aplicar_formato(names.get_first_name(), formato)
        apellido = aplicar_formato(names.get_last_name(), formato)
        usuario = f"{nombre}{apellido}".replace(' ', '').replace('_', '')
        password = f"{usuario}{random.randint(1000, 9999)}"
        pares.add(f"{usuario}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nick_password_anio(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        apellido = aplicar_formato(names.get_last_name(), formato)
        password = f"{apellido}{random.randint(2000, 2023)}"
        pares.add(f"{apellido}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nick_anio_igual(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        apellido = aplicar_formato(names.get_last_name(), formato)
        anio = random.randint(2000, 2023)
        pares.add(f"{apellido}:{anio}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nick_nick_igual(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        apellido = aplicar_formato(names.get_last_name(), formato)
        pares.add(f"{apellido}:{apellido}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nick_apellido_nick(cantidad, formato):
    pares = set()
    while len(pares) < cantidad:
        apellido = aplicar_formato(names.get_last_name(), formato)
        password = f"{apellido.lower()}{apellido}"
        pares.add(f"{apellido}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

def generar_nombre_password_longitud(cantidad, formato):
    while True:
        try:
            largo = int(input(f"{Fore.YELLOW}¿De cuántos dígitos quieres la contraseña? (4-12): {Style.RESET_ALL}"))
            if 4 <= largo <= 12:
                break
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Ingresa un número entre 4 y 12.{Style.RESET_ALL}")
    pares = set()
    while len(pares) < cantidad:
        usuario = aplicar_formato(names.get_first_name(), formato)
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        barra_progreso(len(pares), cantidad)
    return list(pares)

# --- Guardar archivo ---
def guardar_archivo(ruta, datos):
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w') as archivo:
            archivo.write('\n'.join(datos))
        print(f"{Fore.GREEN}¡Listo! Guardado en: {ruta}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error al guardar el archivo: {e}{Style.RESET_ALL}")

def main():
    mostrar_banner()  # Muestra tu banner al inicio

    print(f"{Fore.MAGENTA}{'═' * 60}")
    print(f"{Fore.YELLOW} GENERADOR DE COMBOS (usuario:contraseña) ".center(60, " "))
    print(f"{Fore.MAGENTA}{'═' * 60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Usuario aleatorio (letras) / Contraseña (números)")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Nombre propio como usuario / Contraseña numérica")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Nombre propio como usuario y contraseña")
    print(f"{Fore.CYAN}4.{Style.RESET_ALL} Nombre+Apellido como usuario / Contraseña numérica")
    print(f"{Fore.CYAN}5.{Style.RESET_ALL} Usuario y contraseña numéricos iguales")
    print(f"{Fore.CYAN}6.{Style.RESET_ALL} Nombre+Apellido como usuario / Contraseña con número")
    print(f"{Fore.CYAN}7.{Style.RESET_ALL} Nick (apellido) / Contraseña con año")
    print(f"{Fore.CYAN}8.{Style.RESET_ALL} Nick (apellido) / Contraseña solo año")
    print(f"{Fore.CYAN}9.{Style.RESET_ALL} Nick (apellido) como usuario y contraseña")
    print(f"{Fore.CYAN}10.{Style.RESET_ALL} Nick (apellido) / Contraseña apellido+nick")
    print(f"{Fore.CYAN}11.{Style.RESET_ALL} Nombre propio como usuario / Contraseña numérica (longitud elegida)")
    print(f"{Fore.RED}0. Salir{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'═' * 60}{Style.RESET_ALL}")

    try:
        opcion = int(input(f"{Fore.YELLOW}Selecciona una opción (0-11): {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}Opción inválida. Cerrando...{Style.RESET_ALL}")
        return

    if opcion == 0 or not 1 <= opcion <= 11:
        print(f"{Fore.RED}Saliendo...{Style.RESET_ALL}")
        return

    print(f"{Fore.GREEN}Formato de los nombres generados:{Style.RESET_ALL}")
    print("1. MAYÚSCULAS")
    print("2. minúsculas")
    print("3. Capitalizados (primera letra en mayúscula)")
    try:
        formato = int(input(f"{Fore.YELLOW}Elige el formato (1-3): {Style.RESET_ALL}"))
        if formato not in [1, 2, 3]:
            formato = 3
    except ValueError:
        formato = 3

    try:
        cantidad = int(input(f"{Fore.YELLOW}¿Cuántas combinaciones quieres generar? {Style.RESET_ALL}"))
        if cantidad <= 0:
            print(f"{Fore.RED}Número inválido. Cerrando...{Style.RESET_ALL}")
            return
    except ValueError:
        print(f"{Fore.RED}Entrada inválida. Cerrando...{Style.RESET_ALL}")
        return

    funciones = [
        generar_usuario_letras_password_numeros,
        generar_nombre_password_random,
        generar_nombre_igual_password,
        generar_nombre_real_password_numeros,
        generar_usuario_password_numerico,
        generar_nombrecompleto_password_num,
        generar_nick_password_anio,
        generar_nick_anio_igual,
        generar_nick_nick_igual,
        generar_nick_apellido_nick,
        generar_nombre_password_longitud
    ]

    pares = funciones[opcion - 1](cantidad, formato)

    print(f"\n{Fore.GREEN}Se generaron {len(pares)} combinaciones únicas (sin duplicados).{Style.RESET_ALL}")
    nombre_archivo = input(f"{Fore.YELLOW}Nombre del archivo para guardar (sin .txt): {Style.RESET_ALL}")
    ruta = f"/sdcard/combo/{nombre_archivo}.txt"
    guardar_archivo(ruta, pares)

    print(f"\n{Fore.CYAN}Proceso finalizado. Puedes cerrar esta ventana.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
    
#pip install streamlit names 