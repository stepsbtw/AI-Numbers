import random
import numpy
import Functions

class Ia:
    def __init__(self):
        self.weights = [[random.uniform(-10,10) for i in range(784)] for j in range(10)]
        self.biases = [random.uniform(-10,10) for i in range(10)]

    def brain(self,inputs): # rede neural, pesos, outputs!
        outputs = [0,0,0,0,0,0,0,0,0,0]
      # simplificacao em forma de matrizes dos loops. 
        outputs = map(Functions.sigmoid,
(numpy.array(numpy.dot(self.weights,inputs))+ numpy.array(self.biases))
        #for i in range(len(outputs)):
            #print(f"acho que {outputs[i]} {i}")
        return outputs
