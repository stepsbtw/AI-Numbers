import os
import numpy
from PIL import Image


DATA_BANK = Image.open(os.path.join('data.png'))

def main():
    inputs = crop_data(DATA_BANK,28,28,100,10)
    # aplicar hash pra facilitar o reconhecimento
    hash = {}
    for i,input in 
    return

def crop_data(data_bank,width,height,qt,columns):
    posx = 0
    posy = 0
    data = []
    for i in range(qt):
        img_rect = (posx,posy,posx+width,posy+height)
        img = data_bank.crop(img_rect)
        data.append(img)
        data[i].save('data_input/'f'input{i}.png')
        posx += width+1 # linhas que dividem os dados
        if i % columns == 0 and i > 0:
            posx = 0
            posy+=height+1

    return data

        
main()