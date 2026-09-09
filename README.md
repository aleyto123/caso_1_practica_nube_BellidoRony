# Caso 1 - Práctica Calificada

### Autor: Bellido Rony
### Fecha: 9/09/2026

## Descripción del proyecto

Este proyecto consiste en una aplicación en Python para descargar videos desde varias plataformas de redes sociales, incluyendo YouTube, Instagram, TikTok, Facebook y LinkedIn.

La aplicación utiliza la librería `yt-dlp`, que permite extraer y descargar contenido multimedia de múltiples fuentes con una configuración simple y eficiente.

## Funcionalidad principal

- Interfaz web Flask para introducir la URL del video.
- Mensajes flash de éxito o error durante la descarga.
- Descarga del contenido en `/app/descargas`.
- Soporte para redes sociales como:
  - YouTube
  - Instagram
  - TikTok
  - Facebook
  - LinkedIn

## Requisitos

- Python 3.10 o superior
- Internet para acceder a los sitios de origen
- ffmpeg instalado en el sistema (si se ejecuta localmente o dentro del contenedor)

## Instalación y ejecución local en Python

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd caso_1_practica_nube_BellidoRony
```

2. Crea un entorno virtual (opcional, pero recomendado):

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

En Linux/macOS:

```bash
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Asegúrate de que `ffmpeg` esté instalado en tu sistema:

- Windows: descarga ffmpeg y agrégalo al PATH.
- Linux:

```bash
sudo apt update
sudo apt install ffmpeg
```

5. Ejecuta la aplicación:

```bash
python app.py
```

6. Abre `http://localhost:5000` en el navegador e introduce la URL del video.

## Estructura del proyecto

```text
.
├── app.py
├── requirements.txt
├── Dockerfile.multistage
├── descargas/
├── README.md
└── .gitignore
```

## Construcción y ejecución con Docker

Este proyecto incluye un archivo `Dockerfile.multistage` con una construcción en varias etapas.

### Construir la imagen Docker

```bash
docker build -f Dockerfile.multistage -t video-downloader .
```

### Ejecutar el contenedor

En PowerShell, crea la carpeta local, publica el puerto web y monta el volumen de descargas:

```powershell
New-Item -ItemType Directory -Force .\descargas | Out-Null
docker run --rm -p 5000:5000 -v "${PWD}\descargas:/app/descargas" video-downloader
```

En CMD:

```cmd
if not exist descargas mkdir descargas
docker run --rm -p 5000:5000 -v "%cd%\descargas:/app/descargas" video-downloader
```

Después, abre `http://localhost:5000` y utiliza el formulario web. El contenedor ya incluye `ffmpeg` y prepara `/app/descargas` para almacenar los archivos descargados.

## Notas importantes

- El uso de descargas automáticas de contenido de terceros puede estar sujeto a las políticas y términos de uso de cada plataforma.
- Verifica la legalidad y la autorización para descargar contenido antes de usar la aplicación.
- Algunas plataformas pueden requerir autenticación o bloquear ciertos tipos de videos.

## Autor

Proyecto desarrollado para la práctica calificada del caso 1.

Autor: Bellido Rony
Fecha: 9/09/2026
