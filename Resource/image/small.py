from PIL import Image
import os

for i in os.listdir("./Software/Resource/image/ori"):

    pic = Image.open(f"Software\\Resource\\image\\ori\\{i}")
    pic = pic.resize((32,32))
    pic.save(f"Software\\Resource\\image\\{i}")