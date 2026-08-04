import os
from yt_dlp import YoutubeDL

# Enlace de YouTube que quieres procesar
youtube_url = "https://www.youtube.com/watch?v=9qnXSEGaAcE"

ydl_opts = {
    'format': 'best',  # Busca la mejor calidad disponible
    'quiet': True,
}

with YoutubeDL(ydl_opts) as ydl:
    try:
        # Extrae la información y el enlace directo de streaming
        info = ydl.extract_info(youtube_url, download=False)
        direct_url = info.get('url', None)
        
        print("--- ENLACE DIRECTO EXTRAÍDO ---")
        print(direct_url)
    except Exception as e:
        print(f"Error al extraer: {str(e)}")
