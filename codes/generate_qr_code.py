import qrcode

qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

data = input("Enter the data to be stored in QR Code:")

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("secret_message.png")

print("QR Code Generated Successfully")

