import qrcode

# Data to encode
data = "https://www.example.com"

# Create QR Code
qr = qrcode.QRCode(
    version=1,  # Version 1 means 21x21 matrix; increase for larger size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box
    border=4,  # Border size
)
qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code created and saved as 'qrcode.png'")
