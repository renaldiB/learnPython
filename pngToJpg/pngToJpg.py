from PIL import Image

img = Image.open("ed.png")
rgb_img = img.convert('RGB')
rgb_img.save('ed.jpg')