import qrcode

# URL que quieres abrir con el QR
url = "https://forms.gle/aU2JQ5DkoFE19RMV8"

# Crear QR
img = qrcode.make(url)

# Guardar imagen
img.save("encuestas.png")

print("QR creado como encuestas.png")
