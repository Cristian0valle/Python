from PIL import Image

imagen = Image.open("perro.png")

imagen = imagen.convert('RGB')
imagen.save("NEW.jpg", quality=30)