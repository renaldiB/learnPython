import pywhatkit as pwk
from PIL import Image

handWrite = input("What Text to Convert: ")

pwk.text_to_handwriting(handWrite, save_to="convertedText.png")

Image.open("convertedText.png")