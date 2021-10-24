class square_generator:
    def __init__(self, a, b, m, x0):
        self.a = a
        self.b = b
        self.m = m
        self.x = x0

    def get_actual(self):
        return self.x / self.m

    def get_next(self):
        self.generate_next()
        return self.get_actual() / self.m

    def generate_next(self):
        self.x = (self.a * self.x + self.b) % self.m
