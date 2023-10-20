import numpy
import math
import crop_data
from PIL import Image
import random
import Functions

images_list = crop_data.images_list()
input_image = images_list[0][0] # por enquanto

def main():
    ias = []
    for i in range(10):
        ias.append(Ia())
    check(ias,images_list,input_image)

def check(ias,images_list,input_image):
    answer = images_list[0].index(input_image)
    print(answer)
    ias_answer = []
    outputs = []
    best = ias[0]
    best_index = 0
    best_outputs = best.brain(input_image)
    best_answer = best_outputs[answer]
    for i in range(1,len(ias)):
        outputs = (ias[i].brain(input_image))
        print(f"sou a ia {i}")
        ias_answer.append(outputs[answer])
        if ias_answer[i-1] > best_answer:
            best = ias[i]
            best_index = i
            best_answer = ias_answer[i-1]
    print(f"a melhor eh a ia {best_index}")
    print(f"{best_answer} de chance de ser 0!")
    
    

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
        #for i in range(len(outputs)):
            #print(f"acho que {outputs[i]} {i}")
        print(f'acho que {outputs[0]} 0')
        return outputs

main()
