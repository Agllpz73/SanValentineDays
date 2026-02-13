import qrcode

# URL que quieres abrir con el QR
url = "https://agllpz73.github.io/SanValentineDays/"

# Crear QR
img = qrcode.make(url)

# Guardar imagen
img.save("mi_qr.png")

print("QR creado como mi_qr.png")
