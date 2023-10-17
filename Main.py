import numpy
import math
import crop_data
from PIL import Image
import random
import Functions

images_list = crop_data.images_list()
input_image = images_list[0][0] # por enquanto

def main():
    for i in range(100):
        ias = Ia()

def check(ias):
    answer = images_list.index(input_image)
    outputs = []
    for i in range(len(ias)):
        outputs[i].append(ias[i].brain())
    

class Ia:
    def __init__(self):
        self.weights = []
        self.biases = []
        for i in range(7840): # inputs * outputs
            self.weights.append(random.uniform(-10,10))
        for i in range(10):
            self.biases.append(random.uniform(-10,10))
        
    def brain(self,input_image):
        input_image = input_image.convert('L') # GREYSCALE
        inputs = numpy.array(input_image) # pixels
        outputs = []
        output_sum = 0
        for i in range(10):
            output_sum = 0
            for j in range(28):
                for k in range(28):
                    weight_index = ((i+1) * (k+1*j+1))-1 # index do output +1 * index da linha * index do elemento tudo -1 pq index.
                    output_sum += ((inputs[j][k]/255) * self.weights[weight_index])
            outputs.append(Functions.sigmoid((output_sum + self.biases[i])/100)) # preciso dos BIAS.
        print(outputs)
        self.activation(outputs)

    def activation(self,outputs):
        for i in range(len(outputs)):
            print(f"acho que {outputs[i]} {i}")
        return outputs, max(outputs), outputs.index(max(outputs))

main()