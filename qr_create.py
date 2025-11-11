import qrcode

url = "https://qr-projem.onrender.com/track"


img = qrcode.make(url)

img.save("qr_code.png")

print("QR succeded created")