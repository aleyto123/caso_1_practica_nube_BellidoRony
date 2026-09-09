import os
from urllib.parse import urlparse

import yt_dlp


OUTPUT_DIR = "descargas"


def descargar_video(url):
    """Descarga un video desde una URL usando yt-dlp."""
    try:
        if not url or not url.strip():
            raise ValueError("La URL está vacía.")

        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("URL inválida.")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        ydl_opts = {
            "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        if not info:
            raise RuntimeError("No se pudo obtener información del video.")

        return os.path.join(OUTPUT_DIR, f"{info['title']}.{info.get('ext', 'mp4')}")

    except ValueError as e:
        print(f"Error de URL: {e}")
        return None
    except Exception as e:
        print(f"Error al descargar el video: {e}")
        return None


if __name__ == "__main__":
    print("Descargador de videos")
    print("Soporta YouTube, Instagram, TikTok, Facebook y LinkedIn.")
    print("Escribe 'salir' en cualquier momento para terminar.\n")

    while True:
        video_url = input("Ingresa la URL del video: ").strip()

        if not video_url:
            print("La URL no puede estar vacía. Inténtalo de nuevo.")
            continue

        if video_url.lower() in {"salir", "exit", "quit", "q"}:
            print("Saliendo del programa...")
            break

        resultado = descargar_video(video_url)
        if resultado:
            print(f"Video guardado en: {resultado}")
        else:
            print("La descarga no pudo completarse. Verifica la URL o tu conexión.")

        continuar = input("¿Deseas descargar otro video? (s/n): ").strip().lower()
        if continuar not in {"s", "si", "yes", "y"}:
            print("Saliendo del programa...")
            break
