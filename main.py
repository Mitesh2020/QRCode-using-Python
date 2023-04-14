import qrcode
#PIL package for formatting QRCode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

#Provide link for which you want to make a QRCode.
qr.add_data("https://github.com/Mitesh2020")

qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("profile.png")
