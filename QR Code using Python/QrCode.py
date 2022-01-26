import pyqrcode
import png
link = "https://www.google.co.in/"
qr_code = pyqrcode.create(link)
qr_code.png("QrCode.png", scale=5)