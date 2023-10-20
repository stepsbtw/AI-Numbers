import os
import numpy
from PIL import Image

DATA_BANK = Image.open(os.path.join('data.png')) # importei a imagem geral

def images_to_inputs(): 
   inputs_list = []
   inputs_list_list = []
   for i in range(100):
      # transformando em array e colocando em greyscale
      image = (Image.open(os.path.join('data_input/'f'input{i}.png')).convert('L'))
      image_array = numpy.array(image)
      for sublist in image_array:
         sublist = [element/255 for element in sublist] # colocando o greyscale em 0 a 1 (antes 0 a 255)
         inputs_list.extend(sublist) # juntando, sublistas.
      inputs_list_list.append(inputs_list)
      inputs_list = []
   return inputs_list_list # uma lista, com listas de inputs/
   

def crop_images(data_bank, width, height, qt, rows): # dividir e salva-las numa pasta.
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
