import segno
from PIL import Image, ImageDraw
import numpy as np

# URL del QR
url = "https://agllpz73.github.io/SanValentineDays/"

# Crear QR
qr = segno.make(url, error='h')
qr.save("qr_temp.png", scale=10, dark="black", light="white")

# Abrir QR
img = Image.open("qr_temp.png").convert("RGBA")
w, h = img.size

# Crear máscara de corazón
mask = Image.new("L", (w, h), 0)
draw = ImageDraw.Draw(mask)

points = []
for t in np.linspace(0, 2*np.pi, 1000):
    x = 16 * np.sin(t)**3
    y = -(13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t))
    points.append((x, y))

# Normalizar puntos
xs = [p[0] for p in points]
ys = [p[1] for p in points]

minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)

norm = [(
    (p[0]-minx)/(maxx-minx)*w,
    (p[1]-miny)/(maxy-miny)*h
) for p in points]

draw.polygon(norm, fill=255)

# Aplicar máscara
img.putalpha(mask)

# Guardar resultado
img.save("qr_corazon.png")

print("QR en forma de corazón creado: qr_corazon.png")
