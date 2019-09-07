import pytesseract
from PIL import Image

fp = open('./default2.png','rb')

image = Image.open(fp)
vcode = pytesseract.image_to_string(image,lang='eng', config='--psm 6 --oem 1 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print(vcode)
