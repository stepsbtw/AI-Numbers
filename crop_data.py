import os
import numpy
from PIL import Image

DATA_BANK = Image.open(os.path.join('data.png'))

def main():
   #crop_data(DATA_BANK, 28, 28, 100, 10)
   # aplicar hash pra facilitar o reconhecimento
   inputs = []
   input_list = []
   for i in range(100):
      inputs.append(Image.open(os.path.join('data_input/'f'input{i+1}.png')))
      
   for i in range(0,100,10):
      input_list.append(inputs[i:i+90:10])

   print(input_list[0])
   return


def crop_data(data_bank, width, height, qt, columns):
   posx = 0
   posy = 0
   for i in range(1, qt + 1):
      img_rect = (posx, posy, posx + width, posy + height)
      img = data_bank.crop(img_rect)
      img.save('data_input/'
               f'input{i}.png')
      posx += width + 1  # linhas que dividem os dados
      if i % columns == 0 and i > 0:
         posx = 0
         posy += height + 1


main()
