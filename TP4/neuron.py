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
        l = []
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip("\n")
                x = line.split(" ")
                l.append(x)
            return l

    def calcul_output_neuron(self, line):
        sigma = (float(line[0]) * self.weights[0] + float(line[1]) * self.weights[1]) - self.bias
        if sigma > 0:
            return 1
        return -1

    def update_neuron(self, line):
        self.bias = self.bias + LEARNING_STEP * (int(line[2]) - self.output) * -0.5
        self.weights[0] = self.weights[0] + LEARNING_STEP * (int(line[2]) - self.output) * float(line[0])
        self.weights[1] = self.weights[1] + LEARNING_STEP * (int(line[2]) - self.output) * float(line[1])


if __name__ == '__main__':
    neuron = Neuron()
    for i in range(100):
        nb_errors = 0
        line = neuron.read_line_file('test.txt')
        line_float = list(np.float_(line))
        for i in range(100):
            l = line_float[i]
            output = neuron.calcul_output_neuron(l)
            print(l)
            print(output)
            if int(output) != int(l[2]):
                neuron.update_neuron(l)
                nb_errors += 1
        print("Nombre d'erreurs : {}".format(nb_errors))
