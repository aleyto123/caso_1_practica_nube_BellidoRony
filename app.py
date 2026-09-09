import os
from urllib.parse import urlparse

from flask import Flask, flash, redirect, render_template_string, request, url_for
import yt_dlp


OUTPUT_DIR = os.getenv("DOWNLOAD_DIR", "/app/descargas")
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-me")

HTML_TEMPLATE = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Descargador de videos</title>
    <style>
        :root { color-scheme: light; font-family: system-ui, sans-serif; }
        body { margin: 0; min-height: 100vh; display: grid; place-items: center;
               background: #eef2f7; color: #172033; }
        main { width: min(92vw, 620px); padding: 2.5rem; background: #fff;
               border: 1px solid #d9e0ea; border-radius: 12px;
               box-shadow: 0 12px 30px rgba(23, 32, 51, .08); }
        h1 { margin-top: 0; margin-bottom: .5rem; }
        p { color: #526078; }
        label { display: block; margin: 1.5rem 0 .5rem; font-weight: 600; }
        input { box-sizing: border-box; width: 100%; padding: .8rem;
                border: 1px solid #b8c2d1; border-radius: 6px; font-size: 1rem; }
        button { margin-top: 1rem; padding: .8rem 1.2rem; border: 0;
                 border-radius: 6px; background: #1769aa; color: #fff;
                 font-size: 1rem; font-weight: 600; cursor: pointer; }
        button:hover { background: #125487; }
        .message { padding: .8rem 1rem; border-radius: 6px; margin: 1rem 0; }
        .success { background: #e6f6ed; color: #176b3a; }
        .error { background: #fdeaea; color: #9b2525; }
    </style>
</head>
<body>
    <main>
        <h1>Descargador de videos</h1>
        <p>Descarga videos compatibles con yt-dlp en el almacenamiento configurado.</p>
        <p>Plataformas compatibles: YouTube, Instagram, TikTok, Facebook y LinkedIn.</p>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% for category, message in messages %}
                <div class="message {{ category }}" role="alert">{{ message }}</div>
            {% endfor %}
        {% endwith %}

        <form method="post">
            <label for="url">URL del video</label>
            <input id="url" name="url" type="url" required
                   placeholder="https://ejemplo.com/video">
            <button type="submit">Descargar Video</button>
        </form>
    </main>
</body>
</html>
"""


def descargar_video(url):
    """Descarga un video desde una URL usando yt-dlp."""
    if not url or not url.strip():
        raise ValueError("La URL está vacía.")

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URL inválida.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ydl_opts = {
        "format": "best[ext=mp4]/best[ext=webm]/best",
        "extractor_args": {"youtube": {"player_client": ["web", "android", "ios"]}},
        "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url.strip(), download=True)

    if not info:
        raise RuntimeError("No se pudo obtener información del video.")

    filename = ydl.prepare_filename(info)
    return os.path.basename(filename)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("url", "").strip()
        try:
            filename = descargar_video(video_url)
            flash(f"Descarga completada: {filename}", "success")
        except ValueError as error:
            flash(f"Error de URL: {error}", "error")
        except Exception as error:
            flash(f"Error al descargar el video: {error}", "error")
        return redirect(url_for("index"))

    return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
