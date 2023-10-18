
import os
import numpy
from PIL import Image

def main():
   DATA_BANK = Image.open(os.path.join('data.png'))

def images_dict(): # coloquei em uma lista
   #crop_images(DATA_BANK, 28, 28, 100, 10)
   images_dict = {}
   images = []
   images_list = []
   for i in range(10):
       for j in range(10):
           images.append(Image.open(os.path.join('data_input/'f'input{10*i+j}.png')))
       images_list.append(images)
       images = []

   for i in range(10):
      images_dict[i] = tuple(images_list[i])
   print(images_dict)
   images_dict[0][1].show()
   return images_dict


def crop_images(data_bank, width, height, qt, rows): # dividi em varias imagens
   posx = 0
   posy = 0
   for i in range(qt):
      img_rect = (posx, posy, posx + width, posy + height)
      img = data_bank.crop(img_rect)
      img.save('data_input/'f'input{i}.png')
      posy += height + 1  # linhas que dividem os dados
      if i % rows == 0 and i > 0:
         posy = 0
         posx += width + 1

main()
