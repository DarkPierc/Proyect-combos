import streamlit as st
import random
import string
import names
import base64
import io
from datetime import datetime

# Configuración de la página para dispositivos móviles
st.set_page_config(
    page_title="Generador de Combos",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para mejorar la apariencia en móviles
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3rem;
        font-weight: bold;
    }
    h1, h2, h3 {
        text-align: center;
    }
    .option-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .option-card:hover {
        transform: scale(1.02);
        background-color: #e6e9ef;
    }
    .download-btn {
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
        margin-top: 20px;
        transition: background-color 0.3s;
    }
    .download-btn:hover {
        background-color: #45a049;
    }
    .banner {
        text-align: center;
        color: #4285F4;
        font-family: monospace;
        font-size: 12px;
        margin-bottom: 20px;
    }
    /* Ajustes para móviles */
    @media (max-width: 768px) {
        .stButton>button {
            height: 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Banner ASCII Art
BANNER = """
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
"""

# Función para aplicar formato al texto
def aplicar_formato(texto, formato):
    if formato == 1:
        return texto.upper()
    elif formato == 2:
        return texto.lower()
    else:
        return texto.capitalize()

# Funciones generadoras de combinaciones
def generar_usuario_letras_password_numeros(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        usuario = aplicar_formato(''.join(random.choices(string.ascii_letters, k=8)), formato)
        password = ''.join(random.choices(string.digits, k=8))
        pares.add(f"{usuario}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nombre_password_random(cantidad, formato, largo):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        usuario = aplicar_formato(names.get_first_name(), formato)
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nombre_igual_password(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        nombre = aplicar_formato(names.get_first_name(), formato)
        pares.add(f"{nombre}:{nombre}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nombre_real_password_numeros(cantidad, formato, largo):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        nombre = aplicar_formato(names.get_first_name(), formato)
        apellido = aplicar_formato(names.get_last_name(), formato)
        usuario = f"{nombre}{apellido}".replace(' ', '').replace('_', '')
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_usuario_password_numerico(cantidad, formato, largo):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        usuario = aplicar_formato(''.join(random.choices(string.digits, k=largo)), formato)
        pares.add(f"{usuario}:{usuario}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nombrecompleto_password_num(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        nombre = aplicar_formato(names.get_first_name(), formato)
        apellido = aplicar_formato(names.get_last_name(), formato)
        usuario = f"{nombre}{apellido}".replace(' ', '').replace('_', '')
        password = f"{usuario}{random.randint(1000, 9999)}"
        pares.add(f"{usuario}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nick_password_anio(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        apellido = aplicar_formato(names.get_last_name(), formato)
        password = f"{apellido}{random.randint(2000, 2023)}"
        pares.add(f"{apellido}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nick_anio_igual(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        apellido = aplicar_formato(names.get_last_name(), formato)
        anio = random.randint(2000, 2023)
        pares.add(f"{apellido}:{anio}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nick_nick_igual(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        apellido = aplicar_formato(names.get_last_name(), formato)
        pares.add(f"{apellido}:{apellido}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nick_apellido_nick(cantidad, formato):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        apellido = aplicar_formato(names.get_last_name(), formato)
        password = f"{apellido.lower()}{apellido}"
        pares.add(f"{apellido}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

def generar_nombre_password_longitud(cantidad, formato, largo):
    pares = set()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(cantidad):
        usuario = aplicar_formato(names.get_first_name(), formato)
        password = ''.join(random.choices(string.digits, k=largo))
        pares.add(f"{usuario}:{password}")
        # Actualizar barra de progreso
        progress = (i + 1) / cantidad
        progress_bar.progress(progress)
        status_text.text(f"Generando... {int(progress * 100)}%")
    
    status_text.text(f"¡Completado! Se generaron {len(pares)} combinaciones únicas.")
    return list(pares)

# Función para descargar el archivo
def get_download_link(texto, nombre_archivo, texto_boton):
    # Crear un archivo en memoria
    buffer = io.BytesIO()
    buffer.write(texto.encode())
    buffer.seek(0)
    
    # Codificar el archivo para descarga
    b64 = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{nombre_archivo}" class="download-btn">{texto_boton}</a>'
    return href

# Interfaz principal
def main():
    # Banner y título
    st.markdown(f'<div class="banner"><pre>{BANNER}</pre></div>', unsafe_allow_html=True)
    st.title("Generador de Combos")
    st.markdown("### Usuario:Contraseña")
    
    # Contenedor principal
    with st.container():
        # Selección de tipo de combo
        st.subheader("Selecciona el tipo de combo")
        
        # Opciones en tarjetas
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("1. Usuario aleatorio / Contraseña numérica", key="btn1"):
                st.session_state.opcion = 1
            if st.button("3. Nombre = Contraseña", key="btn3"):
                st.session_state.opcion = 3
            if st.button("5. Usuario = Contraseña (numéricos)", key="btn5"):
                st.session_state.opcion = 5
            if st.button("7. Nick / Contraseña con año", key="btn7"):
                st.session_state.opcion = 7
            if st.button("9. Nick = Contraseña", key="btn9"):
                st.session_state.opcion = 9
            if st.button("11. Nombre / Contraseña numérica", key="btn11"):
                st.session_state.opcion = 11
        
        with col2:
            if st.button("2. Nombre / Contraseña numérica", key="btn2"):
                st.session_state.opcion = 2
            if st.button("4. Nombre+Apellido / Contraseña numérica", key="btn4"):
                st.session_state.opcion = 4
            if st.button("6. Nombre+Apellido / Contraseña con número", key="btn6"):
                st.session_state.opcion = 6
            if st.button("8. Nick / Contraseña solo año", key="btn8"):
                st.session_state.opcion = 8
            if st.button("10. Nick / Contraseña apellido+nick", key="btn10"):
                st.session_state.opcion = 10
        
        # Inicializar la opción si no existe
        if 'opcion' not in st.session_state:
            st.session_state.opcion = 0
        
        # Mostrar la opción seleccionada
        if st.session_state.opcion > 0:
            opciones = [
                "Usuario aleatorio (letras) / Contraseña (números)",
                "Nombre propio como usuario / Contraseña numérica",
                "Nombre propio como usuario y contraseña",
                "Nombre+Apellido como usuario / Contraseña numérica",
                "Usuario y contraseña numéricos iguales",
                "Nombre+Apellido como usuario / Contraseña con número",
                "Nick (apellido) / Contraseña con año",
                "Nick (apellido) / Contraseña solo año",
                "Nick (apellido) como usuario y contraseña",
                "Nick (apellido) / Contraseña apellido+nick",
                "Nombre propio como usuario / Contraseña numérica (longitud elegida)"
            ]
            st.info(f"Opción seleccionada: {opciones[st.session_state.opcion-1]}")
            
            # Formato de los nombres
            st.subheader("Formato de los nombres")
            formato = st.radio(
                "Elige el formato:",
                ["MAYÚSCULAS", "minúsculas", "Capitalizados"],
                index=2,
                horizontal=True
            )
            
            formato_num = 1 if formato == "MAYÚSCULAS" else (2 if formato == "minúsculas" else 3)
            
            # Cantidad de combinaciones
            st.subheader("Cantidad de combinaciones")
            cantidad = st.slider("¿Cuántas combinaciones quieres generar?", 10, 10000, 100)
            
            # Parámetros adicionales según la opción
            largo = None
            if st.session_state.opcion in [2, 4, 11]:
                largo = st.slider("Longitud de la contraseña", 4, 12, 8)
            elif st.session_state.opcion == 5:
                largo = st.slider("Longitud del usuario y contraseña", 4, 12, 8)
            
            # Botón para generar
            if st.button("GENERAR COMBO", type="primary"):
                with st.spinner("Generando combinaciones..."):
                    # Llamar a la función correspondiente
                    if st.session_state.opcion == 1:
                        pares = generar_usuario_letras_password_numeros(cantidad, formato_num)
                    elif st.session_state.opcion == 2:
                        pares = generar_nombre_password_random(cantidad, formato_num, largo)
                    elif st.session_state.opcion == 3:
                        pares = generar_nombre_igual_password(cantidad, formato_num)
                    elif st.session_state.opcion == 4:
                        pares = generar_nombre_real_password_numeros(cantidad, formato_num, largo)
                    elif st.session_state.opcion == 5:
                        pares = generar_usuario_password_numerico(cantidad, formato_num, largo)
                    elif st.session_state.opcion == 6:
                        pares = generar_nombrecompleto_password_num(cantidad, formato_num)
                    elif st.session_state.opcion == 7:
                        pares = generar_nick_password_anio(cantidad, formato_num)
                    elif st.session_state.opcion == 8:
                        pares = generar_nick_anio_igual(cantidad, formato_num)
                    elif st.session_state.opcion == 9:
                        pares = generar_nick_nick_igual(cantidad, formato_num)
                    elif st.session_state.opcion == 10:
                        pares = generar_nick_apellido_nick(cantidad, formato_num)
                    elif st.session_state.opcion == 11:
                        pares = generar_nombre_password_longitud(cantidad, formato_num, largo)
                    
                    # Guardar en la sesión
                    st.session_state.pares = pares
                    st.session_state.generado = True
            
            # Mostrar resultados y opción de descarga
            if 'generado' in st.session_state and st.session_state.generado:
                st.subheader("Vista previa")
                # Mostrar una muestra de los resultados
                muestra = st.session_state.pares[:10]
                for par in muestra:
                    st.code(par, language="text")
                
                if len(st.session_state.pares) > 10:
                    st.info(f"... y {len(st.session_state.pares) - 10} más")
                
                # Nombre del archivo
                nombre_archivo = st.text_input("Nombre del archivo (sin .txt)", 
                                              value=f"combo_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
                
                # Contenido del archivo
                contenido = '\n'.join(st.session_state.pares)
                
                # Botón de descarga
                st.markdown(
                    get_download_link(contenido, f"{nombre_archivo}.txt", "📥 DESCARGAR COMBO"),
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()