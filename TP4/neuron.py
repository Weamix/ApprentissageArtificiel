import numpy as np

LEARNING_STEP = 0.01


class Neuron:
    def __init__(self, bias=0.5, nb_weights=2):
        self.output = 0
        self.bias = 0.5
        self.weights = []
        for i in range(nb_weights):
            r = np.random.uniform(0, 1)
            self.weights.append(r)

    def read_line_file(self, file):
        with open(file, 'r') as file:
            for line in file:
                line = line.split()
            return line

    def calcul_output_neuron(self, line):
        theta = (line[0] * self.weights[0] + line[1] * self.weights[1]) - self.bias
        if theta > 0:
            y = 1
        else:
            y = -1
        print(y)
        return y

    def update_neuro(self,exemple,line):
        self.bias = self.bias + LEARNING_STEP * (line[3] - self.output)
        self.weights[0] = self.weights[0] + LEARNING_STEP * (line[3] - self.output) * line[0]
        self.weights[1] = self.weights[1] + LEARNING_STEP * (line[3] - self.output) * line[1]


if __name__ == '__main__':
    neuron = Neuron(1)
    for i in range(100):
        nb_errors = 0
        line = neuron.read_line_file('data.txt')
        output = neuron.calcul_output_neuron(line)
        if output != line[3]:
            neuron.update_neuro(line)
            nb_errors += 1
    print(nb_errors)
