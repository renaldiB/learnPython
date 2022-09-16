from PIL import Image

def Images_Pdf(fileName, output) :
    images = []
    
    for file in fileName:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
        images[0].save(output, save_all=True, append_images=images[1:])
        
Images_Pdf(["dubu.jpg", "ed.png", "owl.png", "pac.jpg", "sb.png"], "Fusion.pdf")
