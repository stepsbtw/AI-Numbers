import random
import numpy
import IA
import Functions
import crop_data

def main():
    inputs_list_list = crop_data.images_to_inputs()
    ias = []
    for i in range(10):
        ias.append(IA.Ia())

    for i in range(len(inputs_list_list)):
        answer = i % 10
        print(f"a imagem eh o numero: {answer} \n")
        ias_answers = []
        for ia in ias:
            outputs = ia.brain(inputs_list_list[i])
            ias_answers.append(outputs[answer])
        best = max(ias_answers)
        print(f'''A melhor resposta foi : {best} de ser {answer}!
        da ia {ias_answers.index(best)}''')

main()
    