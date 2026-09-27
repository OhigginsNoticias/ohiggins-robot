import feedparser
import requests
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# --- CONFIGURACION O'HIGGINS NOTICIAS ---
FUENTES = [
    "https://www.elrancaguino.cl/feed/",
    "https://www.biobiochile.cl/lista/busqueda/?q=ohiggins&rss=1"
]

def obtener_noticia():
    for fuente in FUENTES:
        try:
            feed = feedparser.parse(fuente)
            if feed.entries:
                titulo = feed.entries[0].title
                link = feed.entries[0].link
                return titulo, link
        except:
            continue
    return "Rancagua: Últimas novedades de la Región de O'Higgins", "https://ohigginsnoticias.cl"

def crear_imagen(texto):
    # Tamaño Instagram Post
    W, H = 1080, 1080
    img = Image.new('RGB', (W, H), color='#0a0a0a')
    draw = ImageDraw.Draw(img)

    # Barras rosadas/moradas de tu plantilla
    draw.rectangle([(0, 0), (W, 30)], fill='#ff1493')
    draw.rectangle([(0, H-30), (W, H)], fill='#ff1493')
    draw.rectangle([(0, 30), (20, H-30)], fill='#8a2be2')

    # Texto O'Higgins Noticias
    try:
        font_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 70)
        font_sub = ImageFont.truetype("DejaVuSans.ttf", 35)
    except:
        font_titulo = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Ajustar texto largo
    lineas = textwrap.wrap(texto, width=25)
    texto_final = "\n".join(lineas)

    # Dibujar
    draw.text((80, 120), "O'HIGGINS\nNOTICIAS", font=font_titulo, fill='white')
    draw.text((80, 400), texto_final, font=font_titulo, fill='white')
    draw.text((80, 900), "www.ohigginsnoticias.cl", font=font_sub, fill='#ff1493')

    img.save('noticia_ohiggins.jpg')
    print("Imagen creada: noticia_ohiggins.jpg")

if __name__ == "__main__":
    titulo, link = obtener_noticia()
    print(f"Noticia encontrada: {titulo}")
    print(f"Link: {link}")
    crear_imagen(titulo)