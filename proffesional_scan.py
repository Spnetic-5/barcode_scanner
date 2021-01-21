from PIL import Image
from pyzbar.pyzbar import decode
image_path = "barcode.jpg"
img = Image.open(image_path)
decode = decode(img)
print(decode)