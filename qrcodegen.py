import qrcode
data = 'Don\'t forget to Learn'
qr = qrcode.QRCode(version=1, box_size=10, border = 2)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'blue', back_color = 'white')
img.save('F:/python/questions/myqrcode.png')