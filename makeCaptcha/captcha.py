from captcha.image import ImageCaptcha
from PIL import Image

capt = ImageCaptcha(width=450, height=200)
inp = input("Enter text for captcha: ")
display = capt.generate(inp)
capt.write(inp, "Captcha.png")

Image.open("Captcha.png")

