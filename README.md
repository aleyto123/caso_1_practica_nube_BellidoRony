# Caso 1 - Práctica Calificada

### Autor: Bellido Rony
### Fecha: 9/09/2026

## Descripción del proyecto

Este proyecto consiste en una aplicación en Python para descargar videos desde varias plataformas de redes sociales, incluyendo YouTube, Instagram, TikTok, Facebook y LinkedIn.

La aplicación utiliza la librería `yt-dlp`, que permite extraer y descargar contenido multimedia de múltiples fuentes con una configuración simple y eficiente.

## Funcionalidad principal

- Ingreso de una URL de video por consola.
- Validación de entrada para evitar URLs vacías.
- Descarga del contenido en una carpeta llamada `descargas/`.
- Soporte para redes sociales como:
  - YouTube
  - Instagram
  - TikTok
  - Facebook
  - LinkedIn
- Bucle de múltiples descargas hasta que el usuario decida salir.

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

6. Cuando se te solicite, ingresa la URL del video y confirma si deseas continuar descargando más videos.

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

```bash
docker run -it --rm video-downloader
```

El contenedor ya incluye `ffmpeg` y prepara el entorno para ejecutar la aplicación.

## Notas importantes

- El uso de descargas automáticas de contenido de terceros puede estar sujeto a las políticas y términos de uso de cada plataforma.
- Verifica la legalidad y la autorización para descargar contenido antes de usar la aplicación.
- Algunas plataformas pueden requerir autenticación o bloquear ciertos tipos de videos.

## Autor

Proyecto desarrollado para la práctica calificada del caso 1.

Autor: Bellido Rony
Fecha: 9/09/2026
