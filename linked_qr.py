
import qrcode

qr = qrcode.QRCode(
    version = 1,
    box_size = 15,
    border = 15
)

data = 'www.youtube.com'
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(
    fill = 'black',
    back_color = 'white'
)
img.save('linked_qr.png')