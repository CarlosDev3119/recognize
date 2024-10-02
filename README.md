# Guía de Instalación de Python y Creación de Entorno Virtual en macOS y Windows

## Tabla de Contenidos
- [Instalación de Python en macOS](#instalación-de-python-en-macos)
- [Instalación de Python en Windows](#instalación-de-python-en-windows)
- [Creación de un Entorno Virtual](#creación-de-un-entorno-virtual)
  - [Crear el Entorno Virtual](#crear-el-entorno-virtual)
  - [Activar el Entorno Virtual](#activar-el-entorno-virtual)
  - [Desactivar el Entorno Virtual](#desactivar-el-entorno-virtual)
# Activar Entorno Virtual e Instalar Dependencias desde `requirements.txt`

## Tabla de Contenidos
- [Activar el Entorno Virtual](#activar-el-entorno-virtual)
- [Instalar Dependencias desde `requirements.txt`](#instalar-dependencias-desde-requirementstxt)

---

## Instalación de Python en macOS

1. **Verificar si Python ya está instalado:**
   - Abre la Terminal (`Cmd + Espacio`, escribe "Terminal" y presiona `Enter`).
   - Ejecuta el siguiente comando:
     ```bash
     python3 --version
     ```
   - Si ves un número de versión, Python ya está instalado. Si no, sigue los pasos siguientes para instalarlo.

2. **Instalar Python con Homebrew (recomendado):**
   - **Instalar Homebrew:** Si no tienes Homebrew instalado, ejecuta el siguiente comando en la Terminal:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - **Instalar Python:** Una vez instalado Homebrew, instala Python ejecutando:
     ```bash
     brew install python
     ```
     
3. **Verificar la instalación:**
   - Después de la instalación, verifica que Python esté correctamente instalado ejecutando:
     ```bash
     python3 --version
     ```
   - Esto debería mostrarte la versión de Python instalada.

---

## Instalación de Python en Windows

1. **Descargar el instalador de Python:**
   - Visita la [página oficial de descargas de Python](https://www.python.org/downloads/windows/).
   - Descarga la última versión del instalador para Windows.

2. **Ejecutar el instalador:**
   - Abre el archivo descargado e **IMPORTANTE**: selecciona la opción "Add Python to PATH".
   - Haz clic en "Install Now" y sigue las instrucciones del instalador.

3. **Verificar la instalación:**
   - Abre el Símbolo del sistema (`Win + R`, escribe `cmd` y presiona `Enter`).
   - Ejecuta el siguiente comando:
     ```bash
     python --version
     ```
   - Esto debería mostrar la versión de Python instalada.

---

## Creación de un Entorno Virtual

Un entorno virtual permite aislar las dependencias de un proyecto en particular para evitar conflictos con otras aplicaciones.

### Crear el Entorno Virtual

1. **Abrir la Terminal (macOS) o el Símbolo del sistema (Windows):**
   - En macOS: Presiona `Cmd + Espacio`, escribe "Terminal" y presiona `Enter`.
   - En Windows: Presiona `Win + R`, escribe `cmd` y presiona `Enter`.

2. **Navegar al directorio del proyecto:**
   - Utiliza el comando `cd` para ir al directorio donde quieres crear el entorno virtual:
     ```bash
     cd /ruta/del/proyecto
     ```

3. **Crear el entorno virtual:**
   - En macOS y Windows, ejecuta el siguiente comando:
     ```bash
     python3 -m venv nombre_del_entorno
     ```
     - Reemplaza `nombre_del_entorno` con el nombre que quieras darle al entorno virtual.

### Activar el Entorno Virtual

4. **Activar el entorno virtual:**
   - **En macOS:**
     ```bash
     source nombre_del_entorno/bin/activate
     ```
   - **En Windows:**
     ```bash
     nombre_del_entorno\Scripts\activate
     ```
   - Una vez activado, deberías ver el nombre del entorno virtual al inicio de tu línea de comandos, lo que indica que el entorno está activo.

### Desactivar el Entorno Virtual

5. **Desactivar el entorno virtual (cuando termines de trabajar):**
   - Para desactivar el entorno virtual, ejecuta:
     ```bash
     deactivate
     ```

---

## Notas adicionales
- Para instalar paquetes dentro de tu entorno virtual, usa `pip`. Por ejemplo:
  ```bash
  pip install nombre_del_paquete




## Activar el Entorno Virtual

1. **Abrir la Terminal (macOS) o el Símbolo del sistema (Windows):**
   - En macOS: Presiona `Cmd + Espacio`, escribe "Terminal" y presiona `Enter`.
   - En Windows: Presiona `Win + R`, escribe `cmd` y presiona `Enter`.

2. **Navegar al directorio del proyecto:**
   ```bash
   cd /ruta/del/proyecto

3. **Activar entorno virtual**
    - En macOS:
    ```bash
   source nombre_del_entorno/bin/activate
    
    ```
    
    - En windows:
    ```bash
   nombre_del_entorno\Scripts\activate

4. **Instalar dependencias**
    ```bash
   pip install -r requirements.txt
