# Generador de Combos - Aplicación Streamlit

Esta aplicación es una versión con interfaz gráfica del generador de combos (usuario:contraseña), optimizada para dispositivos móviles y desarrollada con Streamlit.

## Características

- Interfaz gráfica intuitiva y adaptada para dispositivos móviles
- 11 tipos diferentes de generación de combos
- Visualización en tiempo real del progreso de generación
- Descarga directa de los combos generados en formato .txt
- Personalización del formato de los nombres (MAYÚSCULAS, minúsculas, Capitalizados)
- Control sobre la cantidad de combinaciones a generar

## Requisitos

- Python 3.6 o superior
- Streamlit
- Names (librería para generar nombres aleatorios)

## Instalación

```bash
pip install streamlit names
```

## Uso

Para ejecutar la aplicación, navega hasta el directorio del proyecto y ejecuta:

```bash
streamlit run app_streamlit.py
```

Esto abrirá la aplicación en tu navegador web predeterminado. Si estás en un dispositivo móvil, puedes acceder a la aplicación a través de la URL que se muestra en la terminal.

## Tipos de Combos

1. **Usuario aleatorio (letras) / Contraseña (números)**: Genera usuarios con letras aleatorias y contraseñas numéricas.
2. **Nombre propio como usuario / Contraseña numérica**: Usa nombres reales como usuarios y contraseñas numéricas.
3. **Nombre propio como usuario y contraseña**: El mismo nombre se usa como usuario y contraseña.
4. **Nombre+Apellido como usuario / Contraseña numérica**: Combina nombre y apellido para el usuario, con contraseña numérica.
5. **Usuario y contraseña numéricos iguales**: Genera usuarios y contraseñas numéricas idénticas.
6. **Nombre+Apellido como usuario / Contraseña con número**: Usuario con nombre+apellido y contraseña con el mismo texto más números.
7. **Nick (apellido) / Contraseña con año**: Usa apellidos como usuarios y contraseñas con años.
8. **Nick (apellido) / Contraseña solo año**: Apellidos como usuarios y solo años como contraseñas.
9. **Nick (apellido) como usuario y contraseña**: El mismo apellido como usuario y contraseña.
10. **Nick (apellido) / Contraseña apellido+nick**: Apellido como usuario y combinación de apellidos como contraseña.
11. **Nombre propio como usuario / Contraseña numérica (longitud elegida)**: Nombres como usuarios y contraseñas numéricas de longitud personalizable.

## Descarga de Combos

Una vez generados los combos, puedes descargarlos como un archivo .txt haciendo clic en el botón "DESCARGAR COMBO". El archivo se guardará con el nombre que especifiques o con un nombre predeterminado que incluye la fecha y hora de generación.