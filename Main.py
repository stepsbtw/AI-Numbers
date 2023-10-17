import numpy
import math
import crop_data
from PIL import Image
import random
import Functions

images_list = crop_data.images_list()
input_image = images_list[0][0] # por enquanto

def main():
    ia = Ia()
    ia.brain(input_image)

class Ia:
    def __init__(self):
        self.weights = []
        self.bias = []
        for i in range(7840): # inputs * outputs
            self.weights.append(numpy.arange(-10,10,0.01))
        for i in range(10):
            self.bias.append(random.randint(-10,10))
        
    def brain(self,input_image):
        input_image = input_image.convert('L') # GREYSCALE
        inputs = numpy.array(input_image) # pixels
        outputs = []
        for i in range(10):
            output_sum = 0 # so pra poder somar certinho
            for j in range(1,28):
                for k in range(1,28):
                    weight_index = ((i+1) * (k*j))-1 # index do output +1 * index da linha * index do elemento tudo -1 pq index.
                    output_sum += (inputs[j][k] * self.weights[weight_index])
            
            outputs.append(numpy.tanh((output_sum + self.bias[i]))) # preciso dos BIAS.
            print(outputs)

main()