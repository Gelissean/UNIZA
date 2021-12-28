from math import exp
import abc


class Funkcia(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def calculate(value):
        raise NotImplemented

    @staticmethod
    @abc.abstractmethod
    def derivative(value):
        raise NotImplemented


class SgnFunction(Funkcia):

    @staticmethod
    def calculate(value):
        return (1 + sign(value)) // 2

    @staticmethod
    def derivative(value):
        if value == 0:
            return None
        return 0


class Sigmoid01Function(Funkcia):
    t = 0.1

    @staticmethod
    def calculate(value):
        hodnota = max(-30, min(5, value))
        return 1 / (1 + exp(-hodnota / Sigmoid01Function.t))

    @staticmethod
    def derivative(value):
        hodnota = max(-30, min(5, value))
        return exp(-hodnota / Sigmoid01Function.t) / (Sigmoid01Function.t * pow(1 + exp(-hodnota / Sigmoid01Function.t), 2))
        val = exp(-value / Sigmoid01Function.t) / (Sigmoid01Function.t * pow(1 + exp(-value / Sigmoid01Function.t),2))
        return sign(val)*0.1


def sign(x):
    return bool(x > 0) - bool(x < 0)


def to_multi(a, size=10):
    out = [0 for i in range(size)]
    out[a[0]] = 1
    return out


def get_index(list):
    max_index = -1
    max_value = -999
    for i in range(len(list)):
        e = list[i]
        if e > max_value:
            max_index = i
            max_value = e
    return [max_index]
