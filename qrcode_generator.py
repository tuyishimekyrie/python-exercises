import qrcode

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data('https://www.google.com')
image = qr.make_image(fill_color='black', back_color='white')
image.save('qrcode.png')