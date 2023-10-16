import os
import numpy
from PIL import Image

def main():
    data_bank = Image.open(os.path.join('data.png'))
    posx = 0
    posy = 0
    data = []
    for i in range(100): # cortando os 100 inputs.
        img_rect = (posx,posy,posx+28,posy+28)
        img = data_bank.crop(img_rect)
        data.append(img)
        data[i].save('data_input/'f'input{i}.png')
        posx += 29 # adicionando 29 pq tem uma linha de 1 pixel entre as imagens.
        if i%10 == 0 and i>0:
            posx = 0
            posy+=29
        

main()