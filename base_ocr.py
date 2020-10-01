from PIL import Image
import pytesseract

#replace image name with location and parsed data will be on console
im = Image.open('1.jpeg')
txt = pytesseract.image_to_string(im , lang = 'eng')
print(txt)


