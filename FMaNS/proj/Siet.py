import random


class Siet:
    def __init__(self, bunky, epsilon=None, gamma=None, repeats=None, output_function=None, training_convert=None):
        self.bunky = bunky
        self.epsilon = epsilon
        self.gamma = gamma
        self.repeats = repeats
        if output_function is None:
            self.output_function = self._output_function
        else:
            self.output_function = output_function
        if training_convert is None:
            self.training_convert = self._training_convert
        else:
            self.training_convert = training_convert

    def krok(self, vstup):
        vysledok = None
        data = vstup
        for stupen in self.bunky:
            vysledok = []
            for bunka in stupen:
                vysledok.append(bunka.spracuj(data))
            data = vysledok
        return self.output_function(vysledok)

    def trenuj(self, vstupy, vystupy):
        assert self.epsilon is not None
        assert self.gamma is not None
        assert self.repeats is not None
        assert len(vstupy) == len(vystupy)
        pocet = 0
        index = 0
        while (pocet < self.repeats):
            #index = random.randint(0, len(vstupy)-1)
            vstup = vstupy[index]
            vystup_ocakavany = vystupy[index]
            vystup = self.krok(vstup)

            do_update = False
            for vysledok in [pow(vystup_ocakavany[i] - vystup[i], 2) for i in range(len(vystup_ocakavany))]:
                if vysledok > self.epsilon:
                    do_update = True
                    break
            if do_update:
                self._update(vstup, self.training_convert(vystup_ocakavany))
                pocet = 0
            else:
                pocet += 1
            index = (index + 1) % len(vstupy)

    def _update(self, inputs, expected_output):
        size = len(self.bunky)
        nova_uroven = []
        stara_uroven = []
        for i in range(size):
            nova_uroven = []

            if i == size - 1:
                y_ = inputs
            else:
                y_ = [bunka.hodnota for bunka in self.bunky[size - i - 2]]

            for j in range(len(self.bunky[size - i - 1])):
                bunka = self.bunky[size - i - 1][j]
                if len(stara_uroven) == 0:
                    s = expected_output[j]
                    y = bunka.hodnota
                    z = bunka.z
                    g_ = bunka.funkcia.derivative(z)
                    fi = 2 * (s - y) * g_
                else:
                    omegy = [self.bunky[size - i][k].vahy[j] for k in range(len(stara_uroven))]
                    sucet = sum([stara_uroven[k] * omegy[k] for k in range(len(omegy))])
                    z = bunka.z
                    g_ = bunka.funkcia.derivative(z)
                    fi = sucet * g_

                delta_w = [ fi * hodnota * self.gamma * random.random() for hodnota in y_]
                bunka.update(delta_w, fi * self.gamma)
                nova_uroven.append(fi)
            stara_uroven = nova_uroven

    def _output_function(self, par):
        return par

    def _training_convert(self, par):
        return par
