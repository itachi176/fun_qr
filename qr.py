import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Will you be my girlfriend, Linh')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")