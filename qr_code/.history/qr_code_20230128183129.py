# install all the libraries needed
# create a function that collects a text and converts it to a QR code
# save the qrcode as an image
# run the function

import qrcode

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')