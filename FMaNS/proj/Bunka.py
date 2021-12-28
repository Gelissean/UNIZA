import random


class Bunka:
    def __init__(self, funkcia, pocet_vstupov=None, vahy=None, theta=None):
        if vahy is None:
            if pocet_vstupov is None:
                raise ValueError
            else:
                #self.vahy = [1/pocet_vstupov for i in range(pocet_vstupov)]
                self.vahy = [random.uniform(-1, 1) for i in range(pocet_vstupov)]
        else:
            self.vahy = vahy
        if theta is None:
            self.theta = 0  # random.uniform(-5, 5)
        else:
            self.theta = theta
        self.funkcia = funkcia
        self.hodnota = None

    def spracuj(self, vstupy):
        z = self.get_z(vstupy)
        self.hodnota = self.funkcia.calculate(z)
        return self.hodnota

    def get_z(self, vstupy):
        self.z = 0
        for i in range(len(vstupy)):
            self.z += self.vahy[i] * vstupy[i]
        self.z += self.theta
        return self.z

    def update(self, deltas_w, delta_theta):
        assert len(deltas_w) == len(self.vahy)
        self.vahy = [self.vahy[i] + deltas_w[i] for i in range(len(deltas_w))]
        self.theta = self.theta + delta_theta
