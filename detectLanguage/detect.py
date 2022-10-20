from langdetect import detect

inp = input("Type the text to detect: ")
print("The language is:", detect(inp)) 