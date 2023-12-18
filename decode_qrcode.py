from pyzbar.pyzbar import decode
from PIL import Image
img = Image.open("F:\python\questions\myqrcode.png")
result = decode(img)
print(result)