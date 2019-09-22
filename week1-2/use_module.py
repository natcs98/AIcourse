import os
from PIL import Image
im=Image.open('Sydney-Opera-House.jpg')
print(im.format,im.size,im.mode)
#im.show()
#chuyen mau
im=im.convert('L')
#xoay
im=im.rotate(45)
#setsize
im=im.resize((128,128))
im.show()