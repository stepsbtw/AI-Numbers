import random
import numpy
import Functions

class Ia:
    def __init__(self):
        self.weights = [[random.uniform(-10,10) for i in range(784)] for j in range(10)]
        self.biases = [random.uniform(-10,10) for i in range(10)]

    def brain(self,input_image):
        input_image = input_image.convert('L') # GREYSCALE
        inputs_list = numpy.array(input_image) # CADA ELEMENTO EH UMA LINHA DE PIXELS DA LISTA
        inputs = []
        for list_ in inputs_list:
            list_ = [element/255 for element in list_] # dividindo todos elementos por 255
            inputs.extend(list_) # juntando tudo em uma unica lista
        outputs = [0,0,0,0,0,0,0,0,0,0]

        for i in range(len(outputs)):
            for weight,bias in zip(self.weights[i],self.biases):
                outputs[i] = Functions.sigmoid((numpy.dot(inputs,weight)+ bias)/100)

        for i in range(len(outputs)):
            print(f"acho que {outputs[i]} {i}")
        #print(f'acho que {outputs[0]} 0')
        return outputs
